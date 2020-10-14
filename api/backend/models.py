import os
import datetime
from flask import abort
from enum import Enum
from flask_bcrypt import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token
from backend import bcrypt, db, fernet, environment
import sqlalchemy

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
        user = User(email=email)
        user.password = password

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
        return check_password_hash(self.password_hash.encode("utf-8"), password)

    def issue_token(self):
        """Issues a jwt token to identify """
        return create_access_token(identity={"email": self.email}, expires_delta=EXPIRED_IN)


class SavedPassword(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True)
    saved_password = db.Column(db.String(128), nullable=False)
    domain = db.Column(db.String(1024), nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey(User.id))

    user = db.relationship(User, foreign_keys=[user_id])
    __table_args__ = (db.UniqueConstraint('domain', 'user_id'),)

    @staticmethod
    def create(email:str, domain:str, password:str) -> 'User':
        """Create a new user."""
        user_id = User.find_user_by_email(email).id

        saved_password_row = SavedPassword(
            user_id=user_id, 
            domain=domain,
        )
        saved_password_row.password = password
        try:
            db.session.add(saved_password_row)
            db.session.commit()

        except sqlalchemy.exc.IntegrityError as e:
            db.session.rollback()
            existing_password = SavedPassword.get(email, domain)
            db.session.delete(existing_password)
            db.session.commit()

            db.session.add(saved_password_row)
            db.session.commit()

        return saved_password_row  # .__dict__ ?
    
    @property
    def password(self):
        return fernet.decrypt(self.saved_password).decode('utf-8')


    @password.setter
    def password(self, new_password):
        self.saved_password = fernet.encrypt(new_password.encode('utf-8'))

    
    @staticmethod
    def get_password(email:str, domain:str)->'User':
        return SavedPassword.get(email, domain).password

    @staticmethod
    def get(email:str, domain:str)->'User':
        user = User.query.filter_by(email=email).first()
        saved_password_row = SavedPassword.query.filter_by(user_id=user.id ,domain=domain).first()
        return saved_password_row

    def __repr__(self):
        return f"PasswordEntity('{self.user_id, self.saved_password, self.domain}')"


def get_user_id(email: str) -> int:
    return get_user(email).id


def get_user(email: str) -> User:
    return User.query.filter_by(email=email).first()

if environment == "development":
    db.drop_all()
    db.create_all()
    User.create("bar.shopen@gmail.com", "secretsecretsecret")