from app.helpers import format_for_table, get_average_test_runs, get_latest_releases,  get_test_runs
from app.models import Release, TestRun
from flask import render_template
from flask import Blueprint


release_blueprint = Blueprint(
    'release', __name__,
    template_folder='templates'
)


@release_blueprint.route('/releases/', methods=['GET', ])
def index():
    # releases = Release.query.order_by(Release.name.desc())
    # releases = [".".join(release.name.split('.')[:2]) for release in releases]
    releases = ["{0}.{1}".format(release.major, release.minor) for release in get_latest_releases()]
    # xy_releases = sorted(set(releases), reverse=True)
    return render_template('releases.html', rows=releases)


@release_blueprint.route('/releases/<major>', methods=['GET', ])
def major(major):
    runs_by_release = TestRun.query.join(
        TestRun.release
    ).filter(
        Release.name.startswith(major)
    ).order_by(
        Release.name.desc(),
        TestRun.name.desc()
    )

    return render_template('major_releases.html', test_runs=runs_by_release)


@release_blueprint.route('/release/<int:id>', methods=['GET', ])
def release(id):
    release = Release.query.filter_by(id=id).first()
    tc_fields = [
        'name',
        'passed',
        'failed',
        'skipped',
        'error'
    ]
    pass_fail_fields = [
        'name',
        'percent_passed',
        'percent_failed',
    ]
    execution_fields = [
        'name',
        'percent_executed',
        'percent_not_executed'
    ]
    test_runs = get_test_runs(release=release)

    avg_runs = get_average_test_runs(release=release)
    tc_data = format_for_table(avg_runs, tc_fields)
    passfail_data = format_for_table(avg_runs, pass_fail_fields)
    execution_data = format_for_table(avg_runs, execution_fields)

    return render_template(
        'release.html',
        testcase=tc_data,
        passfail=passfail_data,
        execution=execution_data,
        release=release,
        rows=test_runs)
