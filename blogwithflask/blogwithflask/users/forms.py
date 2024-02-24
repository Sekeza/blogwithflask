from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from blogwithflask.users.models import User

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    email =  StringField('Email', validators=[DataRequired(), Email(), Length(min=3, max=20)])
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    confirm_password =  PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')]) 
    submit = SubmitField('Sign Up') 

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data) 
        if user:
            raise ValidationError('The username is already taken. Please choose a different one!') 
        
    def validate_email(self, email):
        user = User.query.filter_by(username=email.data) 
        if user:
            raise ValidationError('The email is already taken. Please choose a different one!') 


class LoginForm(FlaskForm):
    email =  StringField('Email', validators=[DataRequired(), Email(), Length(min=3, max=20)])
    password =  PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')   



