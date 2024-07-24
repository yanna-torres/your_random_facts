from flask import jsonify, Blueprint, request
import requests
import datetime
from models.fact import RandomFact
from repository.user_dao import UserDAO

fact_bp = Blueprint('facts', __name__)

@fact_bp.route('/facts/today', methods=['GET'])
def get_fact_of_the_day():
    response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/today')
    if response.status_code == 200:
        fact = response.json()
        return jsonify(fact)
    else:
        return jsonify({'error': 'Error getting fact of the day'}), 500
    
@fact_bp.route('/facts/random', methods=['GET'])
def get_random_fact():
    response = requests.get('https://uselessfacts.jsph.pl/api/v2/facts/random')
    if response.status_code == 200:
        fact = response.json()
        return jsonify(fact)
    else:
        return jsonify({'error': 'Error getting random fact'}), 500
    
@fact_bp.route('/facts/save', methods=['POST'])
def save_fact(username: str):
    body = request.get_json()
    username = body.get('username')
    fact = body.get('fact')
    user = UserDAO().get_user_by_username(username)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Save fact to database
    fact_object = RandomFact(user.id, fact.get('id'), str(datetime.datetime.now()), fact.get('text'), fact.get('source'))
    
    
    return jsonify({'message': 'Fact saved'}), 201