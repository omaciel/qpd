import os

DEBUG = True
SECRET_KEY = 'quality is free!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data-dev.sqlite3')
