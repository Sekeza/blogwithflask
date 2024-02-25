import os, secrets
from PIL import Image
from flask import Blueprint, render_template, url_for, redirect, flash, request
import email_validator
from blogwithflask import bcrypt, db, app
from blogwithflask.users.forms import RegisterForm, LoginForm, updateAccountForm
from blogwithflask.users.models import User
from flask_login import login_user, current_user, logout_user

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
            login_user(user, remember=form.remember.data)
            return redirect(url_for('users.home'))
            
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            return redirect(url_for('users.login'))
    return render_template('login.html', title='Login Page', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


def save_picture(form_picture):
    hex_random_num = secrets.token_hex(8)
    _, file_ext = os.path.splitext(form_picture.filename)
    picture_filename = hex_random_num + file_ext
    picture_path = os.path.join(app.root_path, 'static/images', picture_filename )
    # form_picture.save(picture_path)

    pic_output_size = (65, 65)
    i = Image.open(form_picture)
    i.thumbnail(pic_output_size)
    i.save(picture_path)

    return picture_filename

@users.route('/account')
def account():
    form = updateAccountForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file 
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    image_file = url_for('static', filename='images/' + current_user.image_file)
    return render_template('account.html', title='Account Page', form=form, image_file=image_file)

