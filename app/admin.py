# coding: utf-8

from flask import abort, redirect, url_for, request
from flask_admin.contrib.sqla import ModelView
from flask_admin import helpers as admin_helpers
from flask_admin import Admin
from flask_security import current_user
from app.models import OperatingSystem, Project, Release, TestRun, User, Role


admin = Admin(
    name='QPD',
    template_mode='bootstrap3',
    base_template='admin_master.html'
)


class BaseView(ModelView):
    """Extends ModelView to add auth support"""

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('admin'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a
        view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                return redirect(url_for('security.login', next=request.url))


class ReleaseView(BaseView):
    column_editable_list = ['major', 'minor', 'patch']
    column_default_sort = ('minor', True)
    column_exclude_list = ('name', )
    column_sortable_list = ('major', 'minor', 'patch')
    form_excluded_columns = ['name', 'testruns']

    def after_model_change(self, form, model, is_created):
        model.update_name()
        self.session.commit()


class TestRunView(BaseView):
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
        BaseView(OperatingSystem, db.session, endpoint='operatingsystems'))
    admin.add_view(BaseView(Project, db.session, endpoint='projects'))
    admin.add_view(ReleaseView(Release, db.session, endpoint='releases'))
    admin.add_view(TestRunView(TestRun, db.session, endpoint='testruns'))

    # security
    admin.add_view(BaseView(User, db.session, endpoint='users',
                            category='Auth'))
    admin.add_view(BaseView(Role, db.session, endpoint='roles',
                            category='Auth'))

    @app.security.context_processor
    def security_context_processor():
        return dict(
            admin_base_template=admin.base_template,
            admin_view=admin.index_view,
            h=admin_helpers,
            get_url=url_for
        )
