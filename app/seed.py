from dateutil import parser

_d = parser.parse

pwd_hash = "$2b$12$QLpUyPzW8PF6Kidk/fMXM.AQQSCI7UK7OsUr4k.2qVAbPq7yPdrhy"
users = [
    {"username": "admin", "email": "1@d.m", "pwd": pwd_hash},
    {"username": "admin2", "email": "2@d.m", "pwd": pwd_hash},
    ]

schools = [
    {
        "title": "CEF 5 Brasília", "release_date": _d("23-May-2023") 
    },
    
    {
        "title": "CEM Setor Leste", "release_date": _d("25-May-2023") 
    },
    
    {
        "title": "CEM Setor Oeste", "release_date": _d("25-May-2023")
    }
    ]

linkages = [
    
    { 'title': 'test', 'school_id': 1, 'student_id':1, 'presence': True},
    
    { 'title': 'test', 'school_id': 2, 'student_id':2, 'presence': True},
    
    ]