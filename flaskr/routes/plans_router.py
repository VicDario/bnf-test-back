from flask import Blueprint
from flaskr.repository.plans_repository import PlansRepository

plans = Blueprint('plans', __name__)

@plans.route('/')
def get_plans():
    plans = PlansRepository.get_all_with_features()
    return plans