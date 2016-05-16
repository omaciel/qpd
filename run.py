#!/usr/bin/env python
import os
from app import create_app, db

if __name__ == '__main__':
    config_name = os.environ.get('FLASK_CONFIG') or 'development'
    print(' * Loading configuration "{0}"'.format(config_name))
    app = create_app(config_name)
    with app.app_context():
        db.create_all()
    app.run()
