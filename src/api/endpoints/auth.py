from flask import Blueprint, request
from models.model import db, User
from core.transaction_result import *
from core.constants import *
import jwt, bcrypt

auth_api = Blueprint('auth_api', __name__)

@auth_api.route('/register', methods=['POST'])
def register():
    try:
        username = request.json.get('username')
        password = request.json.get('password')
        email = request.json.get('email')
        name = request.json.get('name')
        last_name = request.json.get('last_name')

        user = User.query.filter_by(username=username).first()
        if user is not None:
            create_response_error("User " + username +" already exists")
        
        # Adding the salt to password (unique for each user)
        salt = bcrypt.gensalt()
        bytes = password.encode('utf-8') 
        hashed = bcrypt.hashpw(bytes, salt) 

        # printing the salt
        print("Salt :")
        print(salt)
        print(type(salt))
        
        # printing the hashed
        print("Hashed")
        print(hashed)
        print(type(hashed))

        user = User(username=username, user_hash=hashed.decode('utf8'), user_salt=salt.decode('utf8'), email=email, name=name, last_name=last_name)
        db.session.add(user)
        db.session.commit()

        return create_response_success("user: " + username + " created successfully")
    except Exception as error:
        return create_response_error(str(error))


def verify_password(plain_password, hashed_password):
    password_byte_enc = plain_password.encode('utf-8')
    hashed_password = hashed_password.encode('utf-8')
    print(hashed_password)
    return bcrypt.checkpw(password_byte_enc, hashed_password)


@auth_api.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()
    if user is None:
        return create_response_error("Invalid username")
    
    if verify_password(password, user.user_hash):
        payload_data = {
            "user_id": user.id,
            "username": username,
            "rol": "admin"
        }

        secret_key = SECRET_KET 

        token = jwt.encode(payload=payload_data,
                                key=secret_key,
                                algorithm="HS256")
        return create_response_success("Success", {"token": token})
    else:
        return create_response_error("Invalid password")
    
    
