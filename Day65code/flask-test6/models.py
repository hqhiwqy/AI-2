from app import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    password = db.Column(db.String(30), nullable=False)
    nickname = db.Column(db.String(50))
    email = db.Column(db.String(30), nullable=False)
    status = db.Column(db.Integer, server_default='1')
