# routes/user.py
from flask import Blueprint

user_bp = Blueprint('user', __name__)

@user_bp.route('/')
def show_user():
    return 'ユーザーページへようこそ！'