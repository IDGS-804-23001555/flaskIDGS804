import os

class Config(object):
    SECRET_KEY = "ClaveSecreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    # Usamos pymysql para conectar con XAMPP
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/idgs804'
    SQLALCHEMY_TRACK_MODIFICATIONS = False