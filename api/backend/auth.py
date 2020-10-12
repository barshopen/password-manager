from flask import jsonify, abort
from flask_bcrypt import generate_password_hash, check_password_hash
from typing import Tuple
from flask_jwt_extended import create_access_token
import datetime
from backend.models import User

def register_user(email:str, password:str, repeat_password:str)-> int:
    """@ret http status code 200, 409, 422
    200 : user created.
    409 : username already exist.
    422 : something's wrong with your password/ username
    """
    # this shouldn't be here...
    if not (email and password and repeat_password):
        abort(422, description="Please make sure to include the following params: username, password, repeat_password")
    elif len(password)<12:
        abort(422, description="Password should be more then 12 characters long and repeat_password should match password")
    elif password != repeat_password:
        abort(422, description="Password should match repeat password field")
    elif User.find_user_by_email(email):
        abort(409, "Username already exist")
    user  = User.create(email, password) 
    if not user:
        return abort(500, "The server encountered an unexpected condition which prevented it from fulfilling the request, please try agian later")
    
    return {"email": email}

def authenticate_user(email:str, passowrd:str)->Tuple:
    user = User.find_user_by_email(email)
    if not(user and user.verify(passowrd)):
        abort(409,"Wrong credentials")
    
    access_token = user.issue_token()
    return jsonify({"email": email, "token": access_token}), 200

