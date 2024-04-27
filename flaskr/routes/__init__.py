from flask import Blueprint
from .help_routes import help
from .plans_router import plans

routes = Blueprint('api', __name__)

routes.register_blueprint(help, url_prefix='/help')
routes.register_blueprint(plans, url_prefix='/plans')