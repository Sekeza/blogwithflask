from flask import Flask

app = Flask(__name__)

from blogwithflask.users.routes import users

app.register_blueprint(users)

