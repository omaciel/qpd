#!/usr/bin/env python
import os
from app import create_app, db
from app.admin import OperatingSystemAdmin, TestRunAdmin
from app.models import OperatingSystem, TestRun

import flask_admin as admin


if __name__ == '__main__':
    config_name = os.environ.get('FLASK_CONFIG') or 'development'
    print(' * Loading configuration "{0}"'.format(config_name))
    app = create_app(config_name)
    app.config['SQLALCHEMY_ECHO'] = True
    with app.app_context():
        db.create_all()
        admin = admin.Admin(
            app,
            name='QPD',
            template_mode='bootstrap2')
        admin.add_view(TestRunAdmin(TestRun, db.session))
        admin.add_view(OperatingSystemAdmin(OperatingSystem, db.session))
    app.run()
