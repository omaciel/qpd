from flask_admin.contrib import sqla


class TestRunAdmin(sqla.ModelView):
    column_display_pk = True


class OperatingSystemAdmin(sqla.ModelView):
    column_display_pk = True
