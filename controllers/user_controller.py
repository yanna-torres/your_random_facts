from flask import jsonify, Blueprint, request
from models.user import User
from repository.user_dao import UserDAO

user_bp = Blueprint('users', __name__)


@user_bp.route('/users', methods=['POST'])
def register():
    if 'username' not in request.form or 'name' not in request.form:
        return jsonify({'error': 'Missing username or name'}), 400
    
    username = request.form.get('username')
    name = request.form.get('name')
    
    user = User(None, name, username)
    # Save user to database
    user_dao = UserDAO()
    created = user_dao.create_user(user)
    if not created:
        return jsonify({'error': 'Error creating user'}), 500
    return jsonify({'message': 'User created'}), 201