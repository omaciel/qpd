from app.models import OperatingSystem, Release, TestRun
from flask import render_template
from flask import Blueprint

import json


dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder='templates'
)


@dashboard_blueprint.route('/')
def index():
    test_runs = TestRun.query.join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc()
        ).limit(10)
    rows = []
    for row in test_runs:
        rows.append([row.name, row.passed, row.failed, row.skipped])

    rows.reverse()

    return render_template(
        'index.html', data=json.dumps(rows), test_runs=test_runs)


@dashboard_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
