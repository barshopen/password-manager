import time
from flask import render_template, url_for, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend import app, db, auth


@app.route('/time')
def get_current_time():
    return {'time': time.time()}

@app.route("/store_password", methods=['POST'])
@jwt_required
def store_password():
    return "hello1"

@app.route("/retrieve_password", methods=['POST'])
@jwt_required
def retrieve_password():
    return "hello"


@app.route("/login", methods=['POST'], strict_slashes=False)
def login():
    form = request.form.to_dict()
    email = form.get('email')
    password = form.get('password')
    return auth.authenticate_user(email, password)


@app.route("/sign_up", methods=['POST'], strict_slashes=False)
def register():
    form = request.form.to_dict()
    print(form)
    name = form.get('name')
    password = form.get('password')
    confirm_password = form.get('confirm_password')
    email = form.get('email')

    user =  auth.register_user(email, password, confirm_password)
    print(user)
    return user
    # return auth.register_user(name, email, password, confirm_password)


@app.route("/hello", methods=['GET'])
@jwt_required
def hello():
    return "hello"
