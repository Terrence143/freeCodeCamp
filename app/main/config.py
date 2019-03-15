import os


postgres_local_base = 'mysql://root:password@localhost/restplus'

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'password')
    DEBUG = False


class DevelopmentConfig(Config):
 
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/restplus'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/restplus'
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/restplus'
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    
    SQLALCHEMY_DATABASE_URI = 'mysql://root:password@localhost/restplus'


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY