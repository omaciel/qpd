# coding: utf-8

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from models import OperatingSystem, Project, Release, TestRun

admin = Admin(name='QPD', template_mode='bootstrap3')


class TestRunView(ModelView):
    column_exclude_list = [
        'total',
        'total_executed',
        'percent_passed',
        'percent_failed',
        'percent_executed',
        'percent_not_executed',
    ]


def configure_admin(app, db):
    admin.init_app(app)
    # Admin pages
    admin.add_view(TestRunView(TestRun, db.session, endpoint='/admin/testrun'))
