import os

DEBUG = True
SECRET_KEY = 'quality is free!'
LOGGER_ENABLED = True
SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data-dev.sqlite3')
