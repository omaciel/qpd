from app.helpers import format_for_table, get_test_runs
from flask import render_template, request
from flask import Blueprint


dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder='templates'
)


@dashboard_blueprint.route('/', methods=['GET', ])
def index():
    # How many items?
    items = request.args.get('items', 10)

    fields = ['timestamp', 'total']
    # TODO: Get the averaged data grouped by timestamp
    test_runs = get_test_runs(items)
    rows = format_for_table(test_runs, fields)

    return render_template(
        'index.html',
        data=rows,
        test_runs=test_runs,
    )


@dashboard_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
