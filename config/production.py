import os

ADMINS = ['you@example.com']
DEBUG = False
SECRET_KEY = 'quality is free!'
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data.sqlite3')
