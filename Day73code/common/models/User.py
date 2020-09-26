from application import db
from werkzeug.security import generate_password_hash


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True, nullable=False)
	login_name = db.Column(db.String(20), nullable=False)
	login_pwd = db.Column(db.String(128), nullable=False)
	status = db.Column(db.Integer, nullable=False)

	def __init__(self, login_name, login_pwd, status=0):
		self.login_name = login_name
		self.login_pwd = generate_password_hash(login_pwd)
		self.status = status
