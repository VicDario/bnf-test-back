from flaskr.db import db, Question

class QuestionsRepository:
    @staticmethod
    def get_all():
        questions = db.session.execute(db.select(Question)).scalars()
        questions = [question for question in questions]
        return [question.serialize() for question in questions]