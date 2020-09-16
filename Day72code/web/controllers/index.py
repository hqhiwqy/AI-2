from flask import Blueprint
from flask import render_template

route_index = Blueprint('index_page', __name__)


@route_index.route('/')
# @route_index.route('/index')
def index():
    return render_template('index.html')