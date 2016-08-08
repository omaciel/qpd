from app.helpers import get_test_runs
from app.models import OperatingSystem
from flask import abort, render_template
from flask import Blueprint


os_blueprint = Blueprint(
    'operatingsystem', __name__,
    template_folder='templates'
)


@os_blueprint.route('/operatingsystems/', methods=['GET', ])
def index():
    oses = OperatingSystem.query.order_by(
        OperatingSystem.name.desc(),
        OperatingSystem.major_version.desc(),
        OperatingSystem.minor_version.desc(),
    )
    return render_template('operatingsystems.html', oses=oses)


@os_blueprint.route('/operatingsystems/<int:id>', methods=['GET', ])
def operatingsystem(id):
    operating_system = OperatingSystem.query.filter_by(id=id).first()
    if operatingsystem is None:
        abort(404)

    test_runs = get_test_runs(op_system=operating_system)

    return render_template(
        'operatingsystem.html',
        name=operating_system.fullname(),
        runs=test_runs
    )


@os_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
