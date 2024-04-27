from flaskr.db import db, Plan

class PlansRepository:
    @staticmethod
    def get_all_with_features():
        plans = db.session.execute(db.select(Plan)).scalars()
        plans = [plan for plan in plans]
        return [plan.serialize() for plan in plans]