from flask import jsonify, Blueprint, request

user_bp = Blueprint('users', __name__)


@user_bp.route('users', methods=['POST'])
def register():
    if 'username' not in request.form or 'name' not in request.form:
        return jsonify({'error': 'Missing username or name'}), 400
    
    username = request.form.get('username')
    name = request.form.get('name')