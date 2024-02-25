from flask import Blueprint, render_template, url_for, redirect, flash
import email_validator
from blogwithflask import bcrypt, db
from blogwithflask.users.forms import RegisterForm, LoginForm
from blogwithflask.users.models import User
from flask_login import current_user

users = Blueprint('users', __name__)

posts = [
    {
        'title': 'First WebApp Post',
        'content': 'Finally getting to produce content with backend and frontend seamlessly',
        'author': 'Zane',
        'date_posted': 'February 14, 2024',
    },
    {
        'title': 'Life as we see',
        'content': 'take a bold step to get there in time',
        'author': 'Kay',
        'date_posted': 'February 15, 2024',
    },
    {
        'title': 'Weather storm and helicopter crashing',
        'content': 'Investigations into the frequent occurrence of air mishap in the North West of America',
        'author': 'Shey',
        'date_posted': 'February 16, 2024',
    }
]

@users.route('/')
def home():
    return render_template('home.html', posts=posts)

@users.route('/about')
def about():
    return render_template('about.html', title='About Page')

@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))

    form = RegisterForm()
    if form.validate_on_submit():
        hash_passwd = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hash_passwd)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}! You can now log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register Page', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('users.home'))
    
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash(f'Welcome {form.email.data}! You can log in.', 'success')
            return redirect(url_for('users.home'))
            
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('users.login'))
    return render_template('login.html', title='Login Page', form=form)

