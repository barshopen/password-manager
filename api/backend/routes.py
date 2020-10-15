import time
from flask import render_template, url_for, jsonify, request, make_response
from flask_jwt_extended import jwt_required, get_jwt_identity
from backend import app, db, auth, passwordStore

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route("/api/get_password", methods=['POST'])
@jwt_required
def get_password():
    jwt_id = get_jwt_identity()
    email = jwt_id.get('email')

    form = request.form.to_dict()
    domain = form.get('domain')

    return passwordStore.retrieve_password(email, domain)

@app.route("/api/add_password", methods=['POST'])
@jwt_required
def add_password():
    jwt_id = get_jwt_identity()
    email = jwt_id.get('email')

    form = request.form.to_dict()
    domain = form.get('domain')
    password = form.get('password')

    return passwordStore.store_password(email, domain, password)


@app.route("/api/login", methods=['POST'], strict_slashes=False)
def login():
    form = request.form.to_dict()
    email = form.get('email')
    password = form.get('password')
    return auth.authenticate_user(email, password)


@app.route("/api/sign_up", methods=['POST'], strict_slashes=False)
def register():
    form = request.form.to_dict()
    print(form)

    name = form.get('name')
    password = form.get('password')
    confirm_password = form.get('confirm_password')
    email = form.get('email')

    return auth.register_user(email, password, confirm_password)


@app.route("/api/hello", methods=['GET'])
@jwt_required
def hello():
    return "hello"
