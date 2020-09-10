from werkzeug.security import generate_password_hash
from app import db


# User模型
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    passwd = db.Column(db.String(100))
    is_valid = db.Column(db.Boolean)

    def __init__(self, username, passwd, is_valid):
        self.username = username
        self.passwd = generate_password_hash(passwd)
        self.is_valid = is_valid
