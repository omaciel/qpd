import os

DEBUG = False
TESTING = True
SECRET_KEY = 'quality is free!'
WTF_CSRF_ENABLED = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(
    os.path.dirname(__file__), '../data-test.sqlite3')
