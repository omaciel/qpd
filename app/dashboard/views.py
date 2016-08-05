from app.db import db
from app.models import OperatingSystem, TestRun
from flask import render_template, request
from flask import Blueprint
from sqlalchemy.sql.functions import func

import json


dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder='templates'
)


@dashboard_blueprint.route('/', methods=['GET', ])
def index():
    # How many items?
    items = request.args.get('items', 10)
    test_runs = TestRun.query.filter_by(waved=False).join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(),
            TestRun.name.desc(),
            OperatingSystem.major_version.desc()
        ).limit(items)
    rows = []
    for row in test_runs:
        rows.append([row.name, row.passed, row.failed, row.skipped])

    rows.reverse()

    # Average numbers
    avg_rows = db.session.query(
        TestRun.name,
        func.avg(TestRun.passed).label('passed'),
        func.avg(TestRun.failed).label('failed'),
        func.avg(TestRun.skipped).label('skipped'),
    ).group_by(
        TestRun.release_id,
        TestRun.name
    ).order_by(
            TestRun.timestamp.desc(),
            TestRun.name.desc(),
        ).limit(items)
    avg_data = []
    for row in avg_rows:
        avg_data.append([row.name, row.passed, row.failed, row.skipped])
    avg_data.reverse()

    return render_template(
        'index.html',
        avg_data=json.dumps(avg_data),
        data=json.dumps(rows),
        test_runs=test_runs,
    )


@dashboard_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
