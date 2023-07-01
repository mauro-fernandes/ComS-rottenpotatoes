from wtforms import StringField, PasswordField, SubmitField

from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, Length, EqualTo, Email, Regexp, Optional

# import email_validator
from flask_login import current_user
from wtforms import ValidationError, validators
from ..models import User


class login_form(FlaskForm):
    # email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    username = StringField(validators=[InputRequired()])
    password = PasswordField(validators=[InputRequired(), Length(min=8, max=72)])
    # Placeholder labels to enable form rendering
    submit_button = SubmitField("Entrar")


class Register_form(FlaskForm):
    username = StringField(
        validators=[
            InputRequired(),
            Length(3, 20, message="Por favor forneça um nome válido"),
            Regexp(
                "^[A-Za-z][A-Za-z0-9_.]*$",
                0,
                "Nomes de usuário devem conter apenas letras, números, pontos ou underscores",
            ),
        ]
    )
    email = StringField(validators=[InputRequired(), Email(), Length(1, 64)])
    password = PasswordField(validators=[InputRequired(), Length(8, 72)])
    confirm_password = PasswordField(
        validators=[
            InputRequired(),
            Length(8, 72),
            EqualTo("password", message="Passwords devem coincidir !"),
        ]
    )
    submit_button = SubmitField("Cadastrar")

    def validate_email(self, email):
        if User.query.filter_by(email=email.data).first():
            raise ValidationError("Email já registrado!")

    def validate_uname(self, uname):
        if User.query.filter_by(username=uname.data).first():
            raise ValidationError("Username já utilizado!")
