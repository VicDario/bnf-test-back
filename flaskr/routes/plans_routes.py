from flask import Blueprint
from flask_cors import cross_origin
from flaskr.repository.plans_repository import PlansRepository

plans = Blueprint('plans', __name__)

@plans.route('/')
@cross_origin(origin='*')
def get_plans():
    plans = PlansRepository.get_all_with_features()
    return plans