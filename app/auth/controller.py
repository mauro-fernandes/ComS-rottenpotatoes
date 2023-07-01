from flask import render_template, redirect, flash, url_for, session

from datetime import timedelta
from sqlalchemy.exc import (
    IntegrityError,
    DataError,
    DatabaseError,
    InterfaceError,
    InvalidRequestError,
)
from werkzeug.routing import BuildError


from flask_bcrypt import check_password_hash

from flask_login import (
    login_user,
    logout_user,
    login_required,
)

from ..webapp import db, bcrypt
from ..models import User
from .forms import login_form, Register_form

from . import bp

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired
from werkzeug.utils import secure_filename

from wtforms import StringField, SubmitField, SelectField, IntegerField

@bp.route("/", methods=("GET", "POST"), strict_slashes=False)
def index():
    return render_template("index.jinja2", title="Home")


@bp.route("/login/", methods=("GET", "POST"), strict_slashes=False)
def login():
    form = login_form()

    if form.validate_on_submit():
        try:
            user = User.query.filter_by(username=form.username.data).first()
            if user is None:
                # In production, it is recommended to use a generic message
                flash("Usuário não encontrado! Caso não tenha cadastro, registre-se!", "danger")
            elif check_password_hash(user.pwd, form.password.data):
                login_user(user)
                return redirect(url_for("main.index"))
            else:
                flash("Nome ou senha inválido!", "danger")
        except Exception as e:
            flash(e, "danger")

    return render_template("auth/login.jinja2", form=form)


@bp.route("/profile/", methods=("GET", "POST"), strict_slashes=False)
def profile():
    return render_template("auth/profile.jinja2")


# Register route
@bp.route("/register/", methods=("GET", "POST"), strict_slashes=False)
def register():
    form = Register_form()
    if form.validate_on_submit():
        try:
            email = form.email.data
            pwd = form.password.data
            username = form.username.data

            newuser = User(
                username=username,
                email=email,
                pwd=bcrypt.generate_password_hash(pwd),
            )

            db.session.add(newuser)
            db.session.commit()
            flash(f"Conta criada com sucesso!", "success")
            return redirect(url_for("login"))

        except InvalidRequestError:
            db.session.rollback()
            flash(f"Algo deu errado!", "danger")
        except IntegrityError:
            db.session.rollback()
            flash(f"Usuário ja existe", "warning")
        except DataError:
            db.session.rollback()
            flash(f"Entrada inválida!", "warning")
        except InterfaceError:
            db.session.rollback()
            flash(f"Erro ao se conectar a base de dados!", "danger")
        except DatabaseError:
            db.session.rollback()
            flash(f"Erro ao se conectar a base de dados!", "danger")
        except BuildError:
            db.session.rollback()
            flash(f"Ocorreu um erro!", "danger")
    return render_template(
        "auth/register.jinja2",
        form=form,
        text="Create account",
        title="Register",
        btn_action="Register account",
    )

# docs&Upload route/controllers ######################################################################

properties = {                                          # TODO: finish this
    "entity_name": "documento",
    "collection_name": "documentos",
    "list_fields": ["id", "student_id", "status", "title", "comments", "created_at", "updated_at"],
}


class PhotoForm(FlaskForm):
    photo = FileField(validators=[FileRequired()])

@bp.route('/docs/', methods=['GET', 'POST'], strict_slashes=False)      # TODO: fix renderization to upload docs
def upload():
    form = PhotoForm()

    if form.validate_on_submit():
        f = form.photo.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.instance_path, 'photo', filename
        ))
        submit = SubmitField('Upload')
        return redirect(url_for('main'))

    docs_sent = db.session.query(User).filter(User.id == 1).first()
    
    return render_template("users/docs.jinja2", form=form, **properties) #, entities=docs_sent) #, docs_sent=docs_sent) ???


@bp.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth.login"))
