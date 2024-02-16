from flask import Blueprint

users = Blueprint('users', __name__)

@users.route('/')
def home():
    return '<h3>This will be the overview or home page.</h3>'
