# coding: utf-8

from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin
from app.models import OperatingSystem, Project, Release, TestRun

admin = Admin(name='QPD', template_mode='bootstrap3')


class ReleaseView(ModelView):
    column_default_sort = ('name', True)


class TestRunView(ModelView):
    form_excluded_columns = [
        'total',
        'total_executed',
        'percent_passed',
        'percent_failed',
        'percent_executed',
        'percent_not_executed',
    ]

    column_editable_list = ['name', 'release', 'operatingsystem', 'project']
    column_filters = ['name', 'project', 'release']
    column_default_sort = ('timestamp', True)

    def after_model_change(self, form, model, is_created):
        model.update_stats()
        self.session.commit()


def configure_admin(app, db):
    admin.init_app(app)
    # Admin pages
    admin.add_view(
        ModelView(OperatingSystem, db.session, endpoint='operatingsystems'))
    admin.add_view(ModelView(Project, db.session, endpoint='projects'))
    admin.add_view(ReleaseView(Release, db.session, endpoint='releases'))
    admin.add_view(TestRunView(TestRun, db.session, endpoint='testruns'))
