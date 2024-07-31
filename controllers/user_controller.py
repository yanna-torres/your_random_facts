from flask import jsonify, Blueprint, request
from models.user import User
from repository.user_dao import UserDAO

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['POST'])
def register():
    data = request.get_json()
    if 'username' not in data or 'name' not in data:
        return jsonify({'error': 'Missing username or name'}), 400
    
    username = data['username']
    name = data['name']
    
    user = User(None, name, username)
    # Save user to database
    user_dao = UserDAO()
    if user_dao.get_user_by_username(username):
        return jsonify({'error': 'Username already exists'}), 400
    created = user_dao.create_user(user)
    if not created:
        return jsonify({'error': 'Error creating user'}), 500
    return jsonify({'message': 'User created'}), 201