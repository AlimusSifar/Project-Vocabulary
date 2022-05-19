from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from . import db
from .utils import salt_generator


class User(db.Model, UserMixin):
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(128), primary_key=True)
    salt = db.Column(db.String(10), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

    def __init__(self, username, email, password) -> None:
        self.username = username
        self.email = email
        self.salt = salt_generator(email)
        self.password = generate_password_hash(f"{password}-{self.salt}", method='sha256')

    def __repr__(self):
        return f"<{type(self).__name__} {self.email}>"

    def get_id(self):
        return self.email

    def has_valid(self, password):
        return check_password_hash(self.password, f"{password}-{self.salt}")


class Word(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    word = db.Column(db.String(50), nullable=False)
    pos = db.Column(db.String(16), nullable=False)

    def __repr__(self):
        return f"<{type(self).__name__} {self.word}, {self.pos}>"


class Meaning(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    meaning = db.Column(db.String(150), nullable=False)
    source = db.Column(db.String(50), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)

    word = db.relationship("Word", backref="meanings", lazy=True)

    def __repr__(self):
        return f"<{type(self).__name__} {self.id}, {self.source}>"


class Example(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    example = db.Column(db.String(256), nullable=False)
    user_id = db.Column(db.String(128), db.ForeignKey('user.email'), nullable=False)
    word_id = db.Column(db.Integer, db.ForeignKey('word.id'), nullable=False)

    user = db.relationship('User', backref='examples', lazy=True)
    word = db.relationship('Word', backref='examples', lazy=True)

    def __repr__(self):
        return f"<{type(self).__name__} {self.id}, {self.user_id}>"
