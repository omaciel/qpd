from app.models import Project
from flask import render_template
from flask import Blueprint


project_blueprint = Blueprint(
    'project', __name__,
    template_folder='templates'
)


@project_blueprint.route('/projects/')
def index():
    projects = Project.query.order_by(Project.name.asc())
    return render_template('projects.html', projects=projects)


@project_blueprint.app_errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404
