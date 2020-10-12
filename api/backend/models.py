import os
from flask import abort
from enum import Enum
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from backend import bcrypt, db
import datetime


EXPIRED_IN = datetime.timedelta(hours=2)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password_hash = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(320), nullable=False)

    def __repr__(self):
        return f"User('{self.email}')"

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password).decode("utf-8")

    @staticmethod
    def create(email: str, password: str) -> 'User':
        """Create a new user."""
        user = User(password_hash="1", email=email)
        user.password(password)

        db.session.add(user)
        db.session.commit()
        return user  # .__dict__ ?

    @staticmethod
    def find_user_by_email(email: str) -> 'User':
        return User.query.filter_by(email=email).first()

    @staticmethod
    def get_user_by_id(id: int) -> 'User':  # do I even need this?
        return User.query.filter_by(id=id).first()

    def verify(self, password):
        print(check_password_hash(self.password_hash.encode("utf-8"), password))
        return check_password_hash(self.password_hash.encode("utf-8"), password)

    def issue_token(self):
        """Issues a jwt token to identify """
        return create_access_token(identity={"email": self.email}, expires_delta=EXPIRED_IN)


class SavedPassword(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    # this is the message sender if is_sender, else it's the  receiver
    is_sender = db.Column(db.Boolean, nullable=False, default=False)
    saved_password = db.Column(db.String(128), nullable=False)
    domain = db.Column(db.String(1024), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    user = db.relationship(User, foreign_keys=[user_id])

    @staticmethod
    def create(email: str, password: str) -> 'User':
        """Create a new user."""
        saved_password_entity =

        db.session.add(user)
        db.session.commit()
        return user  # .__dict__ ?


def get_user_id(email: str) -> int:
    return get_user(email).id


def get_user(email: str) -> User:
    return User.query.filter_by(email=email).first()


# some initial data to help me debug
db.drop_all()
db.create_all()
