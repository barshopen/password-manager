import configparser
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from cryptography.fernet import Fernet

app = Flask(__name__)

config = configparser.ConfigParser()
config.read('.config')
print(config.sections())
if 'SECRETS' not in config:
    raise Exception(
        ".config file isn't structured properly, please look at .config-TEMPLATE for help")

app.config['JWT_SECRET_KEY'] = config['SECRETS']['LoginManagerKey']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


bcrypt = Bcrypt(app)
jwt = JWTManager(app)

key = config['SECRETS']['SymetricKeyBytes'].encode("utf-8")

fernet = Fernet(key)

print("hi")
print(__name__)
from backend import routes  # nopep8
from backend import models  # nopep8
