from db import get_db, get_cursor
from utils import serialize_user, validate_user_data
from flask import jsonify
import re

def is_valid_email(email):
    # Basic email format check
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_strong_password(password):
    return password and len(password) >= 6

def get_all_users_service():
    try:
        cursor = get_cursor()
        cursor.execute("SELECT id, name, email FROM users")
        users = cursor.fetchall()
        return jsonify([serialize_user(u) for u in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_user_service(user_id):
    try:
        cursor = get_cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE id = ?", (user_id,))
        user = cursor.fetchone()
        if user:
            return jsonify(serialize_user(user)), 200
        else:
            return jsonify({"error": "User not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def create_user_service(data):
    try:
        valid, msg = validate_user_data(data)
        if not valid:
            return jsonify({"error": msg}), 400
        if not is_valid_email(data['email']):
            return jsonify({"error": "Invalid email format"}), 400
        if not is_strong_password(data['password']):
            return jsonify({"error": "Password must be at least 6 characters"}), 400
        cursor = get_cursor()
        cursor.execute("SELECT id FROM users WHERE email = ?", (data['email'],))
        if cursor.fetchone():
            return jsonify({"error": "Email already exists"}), 409
        cursor.execute("INSERT INTO users (name, email, password) VALUES (?, ?, ?)", (data['name'], data['email'], data['password']))
        get_db().commit()
        return jsonify({"message": "User created"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def update_user_service(user_id, data):
    try:
        name = data.get('name')
        email = data.get('email')
        if not all([name, email]):
            return jsonify({"error": "Missing required fields"}), 400
        if not is_valid_email(email):
            return jsonify({"error": "Invalid email format"}), 400
        cursor = get_cursor()
        # Check for duplicate email (excluding current user)
        cursor.execute("SELECT id FROM users WHERE email = ? AND id != ?", (email, user_id))
        if cursor.fetchone():
            return jsonify({"error": "Email already exists"}), 409
        cursor.execute("UPDATE users SET name = ?, email = ? WHERE id = ?", (name, email, user_id))
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        get_db().commit()
        return jsonify({"message": "User updated"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def delete_user_service(user_id):
    try:
        cursor = get_cursor()
        cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
        if cursor.rowcount == 0:
            return jsonify({"error": "User not found"}), 404
        get_db().commit()
        return jsonify({"message": f"User {user_id} deleted"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def search_users_service(name):
    if not name:
        return jsonify({"error": "Please provide a name to search"}), 400
    try:
        cursor = get_cursor()
        cursor.execute("SELECT id, name, email FROM users WHERE name LIKE ?", (f"%{name}%",))
        users = cursor.fetchall()
        return jsonify([serialize_user(u) for u in users]), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def login_service(data):
    try:
        email = data.get('email')
        password = data.get('password')
        if not all([email, password]):
            return jsonify({"status": "failed", "error": "Missing credentials"}), 400
        if not is_valid_email(email):
            return jsonify({"status": "failed", "error": "Invalid email format"}), 400
        cursor = get_cursor()
        cursor.execute("SELECT id FROM users WHERE email = ? AND password = ?", (email, password))
        user = cursor.fetchone()
        if user:
            return jsonify({"status": "success", "user_id": user[0]}), 200
        else:
            return jsonify({"status": "failed"}), 401
    except Exception as e:
        return jsonify({"status": "failed", "error": str(e)}), 500
