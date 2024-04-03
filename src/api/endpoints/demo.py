from flask import Blueprint, jsonify

demo_api = Blueprint('demo_api', __name__)

@demo_api.route('/increment/<int:number>/', methods=['GET'])
def incrementer(number):
    return jsonify({"result": "Incremented number is " + str(number+1)})
