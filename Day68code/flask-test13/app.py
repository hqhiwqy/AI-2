from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config.default_setting')

db = SQLAlchemy(app)