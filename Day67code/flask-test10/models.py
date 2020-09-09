from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    nickname = db.Column(db.String(50))
    email = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Integer, server_default='0')

    def __init__(self):
        self.status = 0

    def to_json(self):
        """返回json格式"""
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'email': self.email

        }
