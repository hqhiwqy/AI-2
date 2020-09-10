from flask import Blueprint, render_template
from models.User import User


admin_route = Blueprint('admin', __name__)


@admin_route.route("/login")
def login():
    """登录"""
    return render_template('/admin/login.html')
