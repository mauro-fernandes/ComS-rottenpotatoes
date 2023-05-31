# This file should contain all the record creation needed to seed the database with its default values.
# The data can then be loaded with the rails db:seed command (or created alongside the database with db:setup).
#
# Examples:
#
#   movies = Movie.create([{ name: 'Star Wars' }, { name: 'Lord of the Rings' }])
#   Character.create(name: 'Luke', movie: movies.first)
#
#   attendances = Attendance.create([{ id: 1 }, { title: 'test' }, {lesson_id=1}, {user_id=1}])
#   Character.create(name: 'Luke', movie: movies.first)
#   Attendance.create(id: 1, title: 'test', lesson_id: 1, user_id: 1)
#   Attendance.create(id: 2, title: 'test2', lesson_id: 2, user_id: 2)


from dateutil import parser

_d = parser.parse

pwd_hash = "$2b$12$QLpUyPzW8PF6Kidk/fMXM.AQQSCI7UK7OsUr4k.2qVAbPq7yPdrhy"
users = [
    {"username": "admin", "email": "1@d.m", "pwd": pwd_hash},
    {"username": "admin2", "email": "2@d.m", "pwd": pwd_hash},
]

movies = [
    {
        "title": "1.Engenharia de Software - 35M12 - Aula 01",  "release_date": _d("23-May-2023") 
    },
    
    {
        "title": "2.Engenharia de Software - 35M12 - Aula 02 ", "release_date": _d("25-May-2023") 
    },
    {   }
]

attendances = [
    
    { 'title': 'test', 'lesson_id': 1, 'student_id':1, 'presence': True},
    
               ]