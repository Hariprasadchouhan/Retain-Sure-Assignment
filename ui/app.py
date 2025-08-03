from flask import Flask, render_template, request, redirect, url_for, flash
import requests

app = Flask(__name__)
app.secret_key = "secret"

API_URL = "http://localhost:5009"

@app.route('/')
def index():
    resp = requests.get(f"{API_URL}/users")
    users = resp.json() if resp.status_code == 200 else []
    return render_template("index.html", users=users)

@app.route('/user/<user_id>')
def user_detail(user_id):
    resp = requests.get(f"{API_URL}/user/{user_id}")
    user = resp.json() if resp.status_code == 200 else None
    return render_template("user_detail.html", user=user)

@app.route('/create', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "email": request.form['email'],
            "password": request.form['password']
        }
        resp = requests.post(f"{API_URL}/users", json=data)
        if resp.status_code == 201:
            flash("User created successfully!", "success")
            return redirect(url_for('index'))
        else:
            flash(resp.json().get("error", "Error creating user"), "danger")
    return render_template("create_user.html")

@app.route('/edit/<user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    if request.method == 'POST':
        data = {
            "name": request.form['name'],
            "email": request.form['email']
        }
        resp = requests.put(f"{API_URL}/user/{user_id}", json=data)
        if resp.status_code == 200:
            flash("User updated!", "success")
            return redirect(url_for('index'))
        else:
            flash(resp.json().get("error", "Error updating user"), "danger")
    resp = requests.get(f"{API_URL}/user/{user_id}")
    user = resp.json() if resp.status_code == 200 else None
    return render_template("edit_user.html", user=user)

@app.route('/delete/<user_id>', methods=['POST'])
def delete_user(user_id):
    resp = requests.delete(f"{API_URL}/user/{user_id}")
    if resp.status_code == 200:
        flash("User deleted!", "success")
    else:
        flash(resp.json().get("error", "Error deleting user"), "danger")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(port=5010, debug=True)
