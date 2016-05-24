import os

from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)

config_name = os.environ.get('FLASK_CONFIG') or 'development'
cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
app.config.from_pyfile(cfg)

# initialize extensions
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

# import blueprints
from app.dashboard.views import dashboard_blueprint

app.register_blueprint(dashboard_blueprint)
