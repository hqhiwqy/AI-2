from application import db
from werkzeug.security import generate_password_hash


class Member(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    member_name = db.Column(db.String(50), nullable=False)
    member_pwd = db.Column(db.String(128), nullable=False)
    status = db.Column(db.Integer)

    def __init__(self, member_name, member_pwd, status=0):
        self.member_name = member_name
        self.member_pwd = generate_password_hash(member_pwd)
        self.status = status
