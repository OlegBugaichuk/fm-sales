DB_CONF = {
    'NAME': 'test',
    'USER': 'project',
    'PASSWORD': 'password',
    'HOST': 'localhost',
}

# SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_CONF['USER']}:{DB_CONF['PASSWORD']}@{DB_CONF['HOST']}:5432/{DB_CONF['NAME']}"
SQLALCHEMY_DATABASE_URL = f"mysql+mysqldb://{DB_CONF['USER']}:{DB_CONF['PASSWORD']}@{DB_CONF['HOST']}:3306/{DB_CONF['NAME']}"

SECRET_KEY = "(k90_^-!a7-1gjs9dmg#4%=-_!rdf3ojyfzyf*44=+xy7mh&d!"