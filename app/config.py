import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '../.env'))


class Config:
    """Basic/base configuration"""

    # General Flask
    WTF_CSRF_ENABLED = False
    STATIC_FOLDER = 'static'
    TEMPLATES_FOLDER = 'templates'
    SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')


class DevConfig(Config):
    """Development configuration"""
    
    FLASK_ENV = 'development'
    DEBUG = True
    TESTING = True

    # Database modifications
    SQLALCHEMY_DATABASE_URI = 'sqlite+pysqlite:///' + os.environ.get('MVP_DB_PATH')
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProdConfig(Config):
    """Production configuration"""
    
    FLASK_ENV = 'production'
    DEBUG = False
    TESTING = False

    # Database modifications
    SQLALCHEMY_DATABASE_URI = ''
    SQLALCHEMY_ECHO = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
