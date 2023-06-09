from flask.cli import AppGroup
from .webapp import db
from .models import School, User, Linkage, Solicitation
from .seed import schools, users, linkages, solicitations 


seed_cli = AppGroup("seed")


@seed_cli.command("schools")
def seed_schools():
    "Add seed data to the database."
    for school in schools:
        db.session.add(School(**school))
    db.session.commit()


@seed_cli.command("users")
def seed_users():
    "Add seed data to the database."
    for user in users:
        db.session.add(User(**user))
    db.session.commit()


@seed_cli.command("linkages")
def seed_linkages():
    "Add seed data to the database."
    for linkage in linkages:
        db.session.add(Linkage(**linkage))
    db.session.commit()
    
@seed_cli.command("solicitations")
def seed_solicitations():
    "Add seed data to the database."
    for solicitation in solicitations:
        db.session.add(Solicitation(**solicitation))
    db.session.commit()