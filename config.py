import os
from os import environ

from dotenv import load_dotenv
load_dotenv()


# 'postgresql://postgres:flask@localhost:5432/user_events'
# os.getenv('DATABASE_URL')
class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_APP="run.py"
    FLASK_DEBUG=1
    FLASK_ENV='development' #включаем отладчика
    SECRET_KEY = os.urandom(32)
    WTF_CSRF_ENABLED = False
    
