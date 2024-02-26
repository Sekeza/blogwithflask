from flask_wtf import FlaskForm
from flask_login import current_user
from flask_wtf.file import FileField, FileAllowed, FileRequired
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
    remember = BooleanField('Remember Me')
    submit = SubmitField('Sign In')   


class updateAccountForm(FlaskForm):
    username = StringField( 'Username', validators=[DataRequired(), Length(min=3, max=20)] )
    email = StringField( 'Email', validators=[ DataRequired(), Email() ] )
    picture = FileField('Update Profile Picture', validators=[ FileRequired(), FileAllowed(['png', 'jpg'], "Wrong format!") ] )
    submit = SubmitField('Update')

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError('That username has been taken, Please choose a different one!')
        
    def validate_email(self, email):
        if email.data != current_user.email:
            user = User.query.filter_by(email=email.data).first()
            if user:
                raise ValidationError('That email has been taken, Please choose a different one!')


