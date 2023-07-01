from dateutil import parser

_d = parser.parse

pwd_hash = "$2b$12$QLpUyPzW8PF6Kidk/fMXM.AQQSCI7UK7OsUr4k.2qVAbPq7yPdrhy"
# users = [
#     {"username": "admin", "email": "1@d.m", "pwd": pwd_hash},
#     {"username": "admin2", "email": "2@d.m", "pwd": pwd_hash},
#     {"username": "pedro", "email":" pedro@unb.br", "pwd": "asdfg", "is_student": False},
#     {"username": "ester", "email": "ester@unb.br", "pwd": "asdfg", "is_student": True},
    
users=[
    {"username": "joao", "email": "joao@unb.br","name": "joao", "pwd": "asdfg", "is_student": True},
    {"username": "davi", "email": "davi@unb.br","name": "Davi", "pwd": "asdfg", "is_student": True},
    {"username": "fernando", "email": "fernando@unb.br","name": "Fernando", "pwd": "asdfg", "is_student": True},
    {"username": "Gustavo", "email": "gustavo@unb.br","name": "Gustavo", "pwd": "asdfg", "is_student": True},
    ]

schools = [
    {       "title": "CEF 5 Brasília" 
    },
    {       "title": "CEM Setor Leste" 
    },
    {       "title": "CEM Setor Oeste"
    },
    {       "title": "Escola da Ponte"
    },
    {       "title": "IFB São Sebastião"
    }, 
    {       "title": "CEF 11 do Gama"
     },
    {       "title": "IFB Riacho Fundo"
     },
    {        "title": "IFB Samambaia"
    },
    {       "title": "IFB Taguatinga"
    },
    {        "title": "IFB Gama"
     },
    {        "title": "IFB Ceilândia"
     },
    {        "title": "IFB Planaltina"
     },
    {       "title": "IFB Recanto das Emas"
    },
    {        "title": "CEM Setor Sul"
    },
    {        "title": "CEM Setor Norte"   
    },
    {        "title": "CEM Setor Central"        
    }
    ]

linkages = [
    
    { 'title': 'test', 'school_id': 1, 'student_id':1 },
    
    { 'title': 'test', 'school_id': 2, 'student_id':2 },
    
    ]

solicitations = [
    
    
    
]