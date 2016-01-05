from flask_wtf import Form
from wtforms.fields import StringField, PasswordField, BooleanField, SubmitField

from wtforms.validators import DataRequired, url, Regexp, Length, EqualTo, Email, ValidationError

from ..models import User

class LoginForm(Form):
    username = StringField('Your Username: ', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')
    
class SignupForm(Form):
    username = StringField('Username', 
                          validators=[ DataRequired(), Length(5, 45),
                                     Regexp('^[A-Za-z0-9_]{3,}$',
                                           message='Username consists of numbers, letters, and underscores')])
    password = PasswordField('Password', validators=[DataRequired(),
                                                    EqualTo('password2', message='Passwords must match.')])
    password2 = PasswordField('Confirm Password', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Length(1,65), Email()])
    submit = SubmitField('Sign Up')
    
    def validate_email(self, email_field):
        if User.query.filter_by(email=email_field.data).first():
            raise ValidationError('An account with this email has already been created.')
        
    def validate_username(self, username_field):
        if User.query.filter_by(username=username_field.data).first():
            raise ValidationError('This username is taken.')
            