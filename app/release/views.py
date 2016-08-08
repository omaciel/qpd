from app.helpers import get_test_runs
from app.models import Release
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
    test_runs = get_test_runs(release=release)

    return render_template('release.html', release=release, rows=test_runs)
