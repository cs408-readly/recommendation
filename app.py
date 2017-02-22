from flask import Flask

from pymongo import MongoClient

app = Flask(__name__)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/api/recommend/<int:user_id>', methods = ['GET'])
def get_recommendation(user_id):
    get_recommendations(user_id)
    return 'Hello user # %d' % user_id

def get_recommendations(user_id):
    """
    Responsible for returning the recommendations to the user
    """

    user_data = get_user_data(user_id)

    all_data = get_user_data()

def get_data(user_id):
    pass

def get_all_data():
    pass

class DataHandler:

    def __init__(self):

        self.client = MongoClient('mongodb://root:password@ds145639.mlab.com:45639/readly')
        self.db = self.client.readly

    def get_data(self, user_id=None):

        users = self.db.users

        if user_id is not None:

            data = users.find_one({ '_id': user_id })

        else:

            cur = users.find()

            data = []
            for doc in cur:
                data.append(doc)

        return data



