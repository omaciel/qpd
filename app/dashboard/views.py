from app.models import OperatingSystem, TestRun
from flask import abort, render_template
from flask import Blueprint


dashboard_blueprint = Blueprint(
    'dashboard', __name__,
    template_folder='templates'
)


@dashboard_blueprint.route('/')
def index():
    test_runs = TestRun.query.join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc())
    return render_template('index.html', runs=test_runs)


@dashboard_blueprint.route('/operatingsystems/', methods=['GET', ])
def operatingsystems():
    oses = OperatingSystem.query.order_by(
        OperatingSystem.name.desc(), OperatingSystem.major_version.desc())
    return render_template('operatingsystems.html', oses=oses)


@dashboard_blueprint.route('/operatingsystems/<int:id>', methods=['GET', ])
def operatingsystem(id):
    operatingsystem = OperatingSystem.query.filter_by(id=id).first()
    if operatingsystem is None:
        abort(404)
    test_runs = TestRun.query.join(
        OperatingSystem).filter_by(id=operatingsystem.id).order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc())

    return render_template(
        'operatingsystem.html',
        name='{0} {1}'.format(
            operatingsystem.name,
            operatingsystem.major_version,
        ),
        runs=test_runs
    )


@dashboard_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
