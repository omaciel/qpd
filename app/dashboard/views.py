from app.helpers import get_last_test_run_per_release, get_latest_releases
from flask import render_template
from flask import Blueprint


dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder='templates'
)


@dashboard_blueprint.route('/', methods=['GET', ])
def index():
    test_runs = []
    releases = get_latest_releases()

    for release in releases:
        for run in get_last_test_run_per_release(release):
            test_runs.append(run)

    return render_template(
        'index.html',
        test_runs=test_runs,
    )


@dashboard_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
