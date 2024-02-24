from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = 'fc5ba26e3c404a3efb44dca49e77520f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)

from blogwithflask.users.routes import users

app.register_blueprint(users)

with app.app_context():
    db.create_all()
