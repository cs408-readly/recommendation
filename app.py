from flask import Flask
from pymongo import MongoClient
from scipy.spatial.distance import cosine

from models.database import DB
from models.user import User

app = Flask(__name__)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/api/recommend/<int:user_id>', methods = ['GET'])
def get_recommendation(user_id):
    return get_recommendations(user_id)

def get_recommendations(user_id):
    """
    Responsible for returning the recommendations to the user
    """

    db = DB()

    Users = User(db)

    user_data = Users.get_preferences(user_id)

    all_data = Users.get_preferences()

    distances = []

    for data in all_data:

        distances.append( (cosine(user_data, data), data) )

    similar_users = sorted(distances, key=lambda x: return x[0])[:10]

    similar_users = np.array(similar_users)

    sum_users = np.sum(similar_users, axis=1)

    return sorted(enumerate(sum_users), key=lambda x: return x[1])

