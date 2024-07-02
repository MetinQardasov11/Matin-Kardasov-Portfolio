from flask import Blueprint

projects_bp = Blueprint('projects', __name__, url_prefix='/projects', template_folder='templates', static_folder='static')

from . import routes