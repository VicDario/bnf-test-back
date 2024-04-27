from flask import Blueprint
from flaskr.repository.questions_repository import QuestionsRepository
help = Blueprint('help', __name__)

@help.route('/')
def get_frequenly_asked_questions():
    questions = QuestionsRepository.get_all()
    return questions