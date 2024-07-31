from flask import jsonify, Blueprint, request, Response
import requests
import datetime
from models.fact import RandomFact
from repository.facts_dao import FactDAO
from repository.user_dao import UserDAO
from proto.fact_pb2 import FactList, Fact, Error 


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
def save_fact():
    body = request.get_json()
    if 'username' not in body or 'fact' not in body:
        return jsonify({'error': 'Missing username or fact'}), 400
    username = body['username']
    fact = body['fact']
    user = UserDAO().get_user_by_username(username)
    print(user)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    
    # Save fact to database
    fact_object = RandomFact(user.id, fact['id'], str(datetime.datetime.now()), fact['text'], fact['source'])
    saved = FactDAO().save_fact(fact_object)
    if not saved:
        return jsonify({'error': 'Error saving fact'}), 500
    return jsonify({'message': 'Fact saved'}), 201

@fact_bp.route('/facts/<username>', methods=['GET'])
def get_facts_by_user(username: str):
    user = UserDAO().get_user_by_username(username)
    if user is None:
        return jsonify({'error': 'User not found'}), 404
    facts = FactDAO().get_facts_by_user(user.id)
    return jsonify([rfact.__dict__ for rfact in facts])

@fact_bp.route('/facts/proto/<username>', methods=['GET'])
def get_facts_by_user_proto(username: str):
    try:
        user = UserDAO().get_user_by_username(username)
        if user is None:
            return jsonify({'error': 'User not found'}), 404
        facts = FactDAO().get_facts_by_user(user.id)
        fact_list = FactList()
        for fact in facts:
            print(fact.__str__()) 

        for fact in facts:
            f = fact_list.facts.add()
            f.id = fact.fact_id
            f.fact = fact.text
            f.user_id = fact.user_id
        return Response(fact_list.SerializeToString(), mimetype='application/octet-stream')
    except Exception as e:
        print(e)
        return jsonify({'error': 'Error getting facts'}), 500
