from flask import Blueprint

plans = Blueprint('plans', __name__)

@plans.route('/')
def get_plans():
    return 'Plans information'