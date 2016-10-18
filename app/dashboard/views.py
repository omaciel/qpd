from app.helpers import get_latest_test_runs
from flask import render_template
from flask import Blueprint


dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder='templates'
)


@dashboard_blueprint.route('/', methods=['GET', ])
def index():
    test_runs = get_latest_test_runs()

    return render_template(
        'index.html',
        test_runs=test_runs,
    )


@dashboard_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
