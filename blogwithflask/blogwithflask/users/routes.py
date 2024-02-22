from flask import Blueprint, render_template, url_for, redirect, flash
import email_validator
from blogwithflask.users.forms import RegisterForm, LoginForm

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
    form = RegisterForm()
    if form.validate_on_submit():
        flash('Welcome user! You can log in.', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register Page', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('users.home'))
    return render_template('login.html', title='Login Page', form=form)

