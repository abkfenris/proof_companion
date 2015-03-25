import os
basedir = os.path.abspath(os.path.dirname(__file__))

from eve_sqlalchemy.decorators import registerSchema

from proof_companion.models import Contact

registerSchema('contact')(Contact)

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret_key'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    EVE_SETTINGS = {
        'DOMAIN' : {
            'contact': Contact._eve_schema['contact']
        },
        'URL_PREFIX' : 'api'
    }


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_RECORD_QUERIES = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://host/database'



class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,

    'default': DevelopmentConfig
}
