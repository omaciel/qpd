from app import db
from flask import render_template
from flask import Blueprint


bp = Blueprint('error', __name__)


@bp.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404


@bp.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500
