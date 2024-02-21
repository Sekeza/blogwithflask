from flask import Flask

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fc5ba26e3c404a3efb44dca49e77520f'

from blogwithflask.users.routes import users

app.register_blueprint(users)

