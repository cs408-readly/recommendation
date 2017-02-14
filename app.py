from flask import Flask

from . import recommend


app = Flask(__name__)


@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify( { 'error': 'Bad request' } ), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)


@app.route('/api/recommend/<int:user_id>', methods = ['GET'])
def get_recommendation(user_id):
    recommend.get_recommendations()
    return 'Hello user # %d' % user_id
