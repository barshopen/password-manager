import configparser
import os
from dotenv import load_dotenv
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from cryptography.fernet import Fernet

load_dotenv()

app = Flask(__name__, static_folder="../../build", static_url_path="/")

environment = os.environ['FLASK_ENV']

config = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())
config.read('configfile')

if 'SECRETS' not in config:
    raise Exception(
        ".config file isn't structured properly, please look at .config-TEMPLATE for help")
app.config['JWT_SECRET_KEY'] = config['SECRETS']['LoginManagerKey']

app.config['SQLALCHEMY_DATABASE_URI'] = config.get(environment, 'SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if environment == "development":
    app.config['SQLALCHEMY_ECHO'] = False



bcrypt = Bcrypt(app)
jwt = JWTManager(app)
db = SQLAlchemy(app)
fernet = Fernet(config['SECRETS']['SymetricKey'].encode("utf-8"))

from backend import routes  # nopep8
from backend import models  # nopep8
