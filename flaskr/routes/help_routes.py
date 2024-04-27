from flask import Blueprint
from flask_cors import cross_origin
from flaskr.repository.questions_repository import QuestionsRepository

help = Blueprint('help', __name__)

@help.route('/')
@cross_origin(origin='*')
def get_frequenly_asked_questions():
    questions = QuestionsRepository.get_all()
    return questions