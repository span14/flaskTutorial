from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from flask_babel import _
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo, Length
from flaskTutorial.models import User

class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired()])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember_me = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Sign In'))


class RegistrationForm(FlaskForm):
    username = StringField(_l("Username"), validators=[DataRequired()])
    email = StringField(_l("Email"), validators=[DataRequired(), Email()])
    password = PasswordField(_l("Password"), validators=[DataRequired(), Length(min=8, max=32)])
    password2 = PasswordField(_l("Repeat Password"), validators=[DataRequired(), EqualTo("password"), Length(min=8, max=32)])
    submit = SubmitField(_l("Register"))

    def validate_username(self, username):
        # TODO: prevent code injection issue
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_('Username has been registered'))
    
    def validate_email(self, email):
        # TODO: prevent code injection issue
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(_("Email has been registered"))

class ResetPasswordRequestForm(FlaskForm):
    email = StringField(_l('Email'), validators=[DataRequired(), Email()])
    submit = SubmitField(_l("Request Password Reset"))

class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l("Password"), validators=[DataRequired, Length(min=8, max=32)])
    password2 = PasswordField(_l("Repeat Password"), validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Request Password Reset'))