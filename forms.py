from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class Registration_Form(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=3, max=50) ])
    email = StringField("email", validators=[DataRequired(), Email() ])
    password = PasswordField("password", validators=[DataRequired(), Length(min=6, message="Password must be at least 8 characters")])
    confirm_password = PasswordField("confirm_password", validators=[DataRequired(), EqualTo("password")])
    submit = SubmitField("Sign up")

class Login_Form(FlaskForm):
    email = StringField("email", validators=[DataRequired(), Email() ])
    password = PasswordField("password", validators=[DataRequired()])
    submit = SubmitField("Login")   