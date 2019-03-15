import os


postgres_local_base = 'postgresql://postgres:password@localhost:5432/RESTplus'

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'password')
    DEBUG = False


class DevelopmentConfig(Config):
 
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/RESTplus'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/RESTplus'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/RESTplus'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:5432/RESTplus'


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY