from flask import Flask
from flask import request
from flask import jsonify
from pymongo import MongoClient
from scipy.spatial.distance import cosine

from models.database import DB
from models.user import User

import numpy as np

app = Flask(__name__)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/recommend', methods = ['POST'])
def get_recommendation():
    user_id = request.form['user_id'][1:-1]
    result = get_recommendations(user_id)
    return jsonify(result)

def get_recommendations(user_id):
    """
    Responsible for returning the recommendations to the user
    """

    db = DB()
    Users = User(db)

    user_data, find_dict = Users.get_preferences(user_id)
    all_data = Users.get_preferences()

    distances = []
    for data in all_data:
        distances.append( (cosine(user_data, data), data) )

    similar_users = sorted(distances, key=lambda x: x[0])[:10]
    similar_users = np.array([user[1] for user in similar_users])
    sum_users = np.sum(similar_users, axis=0)

    results = sorted(enumerate(sum_users), key=lambda x: x[1], reverse=True)[:10]
    return_val = [find_dict[result[0]] for result in results]

    return return_val

app.run()
