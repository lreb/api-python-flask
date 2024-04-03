from flask import Blueprint, jsonify
welcome_api = Blueprint('welcome_api', __name__)

@welcome_api.route('/hello')
def welcome():
    return jsonify({"result": "Hello World!"})

@welcome_api.route('/hello/<string:name>/')
def hello(name):
    return jsonify({"result": "Hello " + name}) 
