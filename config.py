import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = "ClaveSecreta"
    SESSION_COOKIE_SECURE = False

class DevelopmentConfig(Config):
    DEBUG = True
    # CAMBIO AQUÍ: Usamos sqlite y definimos la ruta del archivo .db
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'proyecto.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False