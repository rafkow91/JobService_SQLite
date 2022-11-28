from os import environ
from dotenv import load_dotenv

load_dotenv()

DB_PATH = environ.get('DB_PATH')
EMAIL_DOMAIN = environ.get('EMAIL_DOMAIN')
PASSWORD_SALT = environ.get('PASSWORD_SALT')