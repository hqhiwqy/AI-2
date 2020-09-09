from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash
db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    nickname = db.Column(db.String(50))
    email = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Integer, server_default='0')

    def __init__(self, name, password, nickname, email, status=0):
        self.name = name
        self.password = generate_password_hash(password)
        self.nickname = nickname
        self.email = email
        self.status = status

    def to_json(self):
        """返回json格式"""
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'email': self.email

        }
