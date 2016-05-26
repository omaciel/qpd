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
from app.operatingsystem.views import os_blueprint
from app.project.views import project_blueprint
from app.testrun.views import run_blueprint

app.register_blueprint(dashboard_blueprint, url_prefix='/')
app.register_blueprint(os_blueprint, url_prefix='/operatingsystems')
app.register_blueprint(project_blueprint, url_prefix='/projects')
app.register_blueprint(run_blueprint, url_prefix='/testruns')
