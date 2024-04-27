from flask import Blueprint

help = Blueprint('help', __name__)

@help.route('/')
def get_frequenly_asked_questions():
    return 'Frequently Asked Questions'