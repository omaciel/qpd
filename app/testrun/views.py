from app.models import OperatingSystem, TestRun
from flask import render_template
from flask import Blueprint


run_blueprint = Blueprint(
    'testrun', __name__,
    template_folder='templates'
)


@run_blueprint.route('/testruns', methods=['GET', ])
@run_blueprint.route('/testruns/<int:page>', methods=['GET', ])
def index(page=1):
    test_runs = TestRun.query.join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc()
        ).paginate(page, 15, False)
    return render_template('testruns.html', runs=test_runs)
