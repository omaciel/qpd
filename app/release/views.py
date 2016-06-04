from app.models import OperatingSystem, Release, TestRun
from flask import render_template
from flask import Blueprint


release_blueprint = Blueprint(
    'release', __name__,
    template_folder='templates'
)


@release_blueprint.route('/releases/', methods=['GET', ])
def index():
    releases = Release.query.order_by(Release.name.desc())
    return render_template('releases.html', rows=releases)


@release_blueprint.route('/releases/<int:id>', methods=['GET', ])
def release(id):
    release = Release.query.filter_by(id=id).first()
    test_runs = TestRun.query.filter_by(release=release).join(
        OperatingSystem).filter().order_by(
            TestRun.timestamp.desc(), OperatingSystem.major_version.desc())
    return render_template('release.html', release=release, rows=test_runs)
