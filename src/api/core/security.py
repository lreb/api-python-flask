from functools import wraps
from flask import request
from models.model import db, User
from core.transaction_result import *
from core.constants import *
import jwt


def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None
        if "Authorization" in request.headers:
            token = request.headers["Authorization"].split(" ")[1]

        if not token:
            #return create_response_error() jsonify({'message': 'Token is missing!'}), 401
            return create_response_error('Token is missing!'), 401
        
        try:
           secret_key = SECRET_KET # 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJPbmxpbmUgSldUIEJ1aWxkZXIiLCJpYXQiOjE3MTIzMzgwNDMsImV4cCI6MTc0Mzg3NDA0MywiYXVkIjoid3d3LmV4YW1wbGUuY29tIiwic3ViIjoianJvY2tldEBleGFtcGxlLmNvbSIsIkdpdmVuTmFtZSI6IkpvaG5ueSIsIlN1cm5hbWUiOiJSb2NrZXQiLCJFbWFpbCI6Impyb2NrZXRAZXhhbXBsZS5jb20iLCJSb2xlIjpbIk1hbmFnZXIiLCJQcm9qZWN0IEFkbWluaXN0cmF0b3IiXX0.R0pYi1FA7NoM1vI56o5a02cQQb5ZA9U7iPbW-SMU4Bo'
           data = jwt.decode(token, secret_key, algorithms=["HS256"])
           current_user = User.query.get(data["user_id"])
           if current_user is None:
                return create_response_error('Invalid Authentication token!'), 401
            #     return {
            #     "message": "Invalid Authentication token!",
            #     "data": None,
            #     "error": "Unauthorized"
            # }, 401
            #if not current_user["active"]:
                #abort(403)
        except Exception as error:
            #return jsonify({"result": "error", "message": str(error)})
            return create_response_error(str(error)), 401
        # Here you would typically check if the token is valid
        # For example, by checking if it's in a list of valid tokens
        # If it's not valid, return a 401 Unauthorized status code

        return f(*args, **kwargs)
    return decorated