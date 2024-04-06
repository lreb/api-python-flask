from flask import Blueprint, jsonify
from core.transaction_result import *

welcome_api = Blueprint('welcome_api', __name__)

@welcome_api.route('/hello')
def welcome():
    return create_response_success("Hello World!")

@welcome_api.route('/hello/<string:name>/')
def hello(name):
    return create_response_success("Hello " + name)
