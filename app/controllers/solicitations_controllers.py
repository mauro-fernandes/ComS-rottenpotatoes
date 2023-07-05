from flask import Blueprint, render_template, request, redirect, url_for, flash
from wtforms import StringField, SubmitField, SelectField, IntegerField
from flask_wtf import FlaskForm
from wtforms.validators import InputRequired, NumberRange

from ..models import Solicitation, School

bp_name = "solicitations"

bp = Blueprint(bp_name, __name__)
from ..webapp import db
import app

properties = {
    "entity_name": "solicitation",
    "collection_name": "Solicitações",
    "list_fields": ["id", "student_id", "school_id", "status", "title", "comments", "created_at", "updated_at"],
}


class _to:
    def __to(method):
        return lambda **kwargs: url_for(f"{bp_name}.{method}", **kwargs)

    index = __to("index")
    show = __to("show")
    edit = __to("edit")
    delete = __to("delete")


class _j:
    index = f"{bp_name}/index.jinja2"
    edit = f"{bp_name}/edit.jinja2"
    show = f"{bp_name}/show.jinja2"
    new = f"{bp_name}/new.jinja2"
    create = f"{bp_name}/create.jinja2"
    search_tmdb = f"{bp_name}/search_tmdb.jinja2"


@bp.route("/", methods=["GET"])
def index():
    """
    Index page.
    :return: The response.
    """
    solicitations = Solicitation.query.all()
    return render_template(_j.index, entities=solicitations, **properties)


class EditForm(FlaskForm):
    title = StringField("Informações", validators=[InputRequired()])
    rating = StringField("Data de inicio sugerida")
    description = StringField("Data de finalização sugerida")
    
    '''
    @School.query.all()
    def load_school(school_id):
        return School.query.get(int(school_id))
    from ..models import School
    school_id = SelectField("school", choices=[(school.id, school.title) for school in School.query.all()])
    '''
    
    school_id = StringField("Escola", validators=[InputRequired()])
    student_id = StringField("Aluno", validators=[InputRequired()])
    status = SelectField("Status", choices=[(False, 'Aceito'), (False, 'Rejeitado'), (True, 'Documentação Pendente')], coerce=bool)   
    comments = StringField("Comentários")
    
    # with app.webapp.app_context():
    #     school = School.query.all()
    #     student = Student.query.all()
    # student = StringField("student")
    # school = StringField(f"school: Put{school.id} for {school.title}")
    
    submit = SubmitField("Enviar")


@bp.route("/new", methods=["GET"])
def new():
    """
    Page to create new Entity
    :return: render create template
    """
    form = EditForm()
    return render_template(_j.new, form=form, **properties)


@bp.route("/", methods=["POST"])
def create():
    """
    Create new entity
    :return: redirect to view new entity
    """
    form = EditForm(formdata=request.form)
    if form.validate_on_submit():
        newsolicitation = Solicitation()
        form.populate_obj(newsolicitation)
        db.session.add(newsolicitation)
        db.session.commit()
        flash(f"'{ newsolicitation.title}' created")
        return redirect(_to.show(id=newsolicitation.id))
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/show", methods=["GET"])
def show(id):
    """
    Show page.
    :return: The response.
    """
    solicitation = db.get_or_404(Solicitation, id)
    return render_template(_j.show, entity=solicitation, **properties)


@bp.route("/<int:id>/edit", methods=["GET"])
def edit(id):
    """
    Edit page.
    :return: The response.
    """
    solicitation = db.get_or_404(Solicitation, id)
    userform = EditForm(formdata=request.form, obj=solicitation)
    return render_template(_j.edit, form=userform, **properties)


@bp.route("/<int:id>/edit", methods=["POST", "UPDATE"])
@bp.route("/<int:id>", methods=["UPDATE"])
def update(id):
    """
    Save Edited Entity
    :return: redirect to show entity
    """
    solicitation = db.get_or_404(Solicitation, id)
    form = EditForm(formdata=request.form, obj=solicitation)
    if form.validate_on_submit():
        form.populate_obj(solicitation)
        db.session.commit()
        flash(f"'{ solicitation.title}' updated")
        return redirect(_to.show(id=id))
    else:
        flash("Error in form validation", "danger")


@bp.route("/<int:id>/delete", methods=["POST", "DELETE"])
def destroy(id):
    """
    Delete Entity
    :return: redirect to list
    """
    solicitation = db.get_or_404(Solicitation, id)
    db.session.delete(solicitation)
    db.session.commit()
    flash(f"'{ solicitation.title}' deleted")
    return redirect(_to.index())
