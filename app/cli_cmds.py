from flask.cli import AppGroup
from .webapp import db
from .models import Movie, User, Attendance
from .seed import movies, users, attendances

seed_cli = AppGroup("seed")


@seed_cli.command("movies")
def seed_movies():
    "Add seed data to the database."
    for movie in movies:
        db.session.add(Movie(**movie))
    db.session.commit()


@seed_cli.command("users")
def seed_users():
    "Add seed data to the database."
    for user in users:
        db.session.add(User(**user))
    db.session.commit()


@seed_cli.command("attendances")
def seed_attendances():
    "Add seed data to the database."
    for attendance in attendances:
        db.session.add(Attendance(**attendance))
    db.session.commit()