from flask import Flask, request, jsonify
from service import (
    get_all_users_service,
    get_user_service,
    create_user_service,
    update_user_service,
    delete_user_service,
    search_users_service,
    login_service
)

app = Flask(__name__)

@app.route('/')
def home():
    return "User Management System", 200

@app.route('/users', methods=['GET'])
def get_all_users():
    return get_all_users_service()

@app.route('/user/<user_id>', methods=['GET'])
def get_user(user_id):
    return get_user_service(user_id)

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json(force=True)
    return create_user_service(data)

@app.route('/user/<user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json(force=True)
    return update_user_service(user_id, data)

@app.route('/user/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    return delete_user_service(user_id)

@app.route('/search', methods=['GET'])
def search_users():
    name = request.args.get('name')
    return search_users_service(name)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json(force=True)
    return login_service(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5009, debug=True)