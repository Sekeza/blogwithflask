from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
app = Flask(__name__)
app.app_context().push()

app.config['SECRET_KEY'] = 'fc5ba26e3c404a3efb44dca49e77520f'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = 'smtp.googlemail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'syglemelg@gmail.com' #os.environ.get('MAIL_USERNAME') 
app.config['MAIL_PASSWORD'] = 'shakingmyhead' #os.environ.get('MAIL_PASSWORD') 
mail = Mail(app)

from blogwithflask.users.routes import users

app.register_blueprint(users)

with app.app_context():
    db.create_all()
