from os import getenv

class Config(object):
    DEBUG = False
    TESTING = False
    DEVELOPMENT = False
    SQLALCHEMY_DATABASE_URI = getenv("DB_URI_CONNECTION")

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True
