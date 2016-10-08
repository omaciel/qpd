import os

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_security import Security, SQLAlchemyUserDatastore
from app.admin import configure_admin
from app.db import db
from app.models import User, Role

# initialize extensions
bootstrap = Bootstrap()


def create_app():
    """
    App factory pattern avoids circular imports, so instead of importing
    'app' directly you import its factory. If you need the current running app
    you can use 'from flask import current_app'
    :return: app
    """
    app = Flask(__name__)
    config_name = os.environ.get('FLASK_CONFIG') or 'development'
    cfg = os.path.join(os.getcwd(), 'config', config_name + '.py')
    app.config.from_pyfile(cfg)

    # initialize extensions
    bootstrap.init_app(app)
    db.init_app(app)

    # security
    user_datastore = SQLAlchemyUserDatastore(db, User, Role)
    app.security = Security(app, user_datastore)

    # import blueprints
    from app.dashboard.views import dashboard_blueprint
    from app.operatingsystem.views import os_blueprint
    from app.project.views import project_blueprint
    from app.release.views import release_blueprint
    from app.testrun.views import run_blueprint

    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(os_blueprint)
    app.register_blueprint(project_blueprint)
    app.register_blueprint(release_blueprint)
    app.register_blueprint(run_blueprint)

    configure_admin(app, db)

    db.create_all(app=app)

    return app
