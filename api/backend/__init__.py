import configparser
import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager

app = Flask(__name__)

app.config.from_envvar('ENV_FILE_LOCATION')
config = configparser.ConfigParser()
config.read('.config')

if 'SECRETS' not in config:
    raise Exception(
        ".config file isn't structured properly, please look at .config-TEMPLATE for help")

app.config['JWT_SECRET_KEY'] = config['SECRETS']['LoginManagerKey']

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)
jwt = JWTManager(app)


from backend import routes  # nopep8
