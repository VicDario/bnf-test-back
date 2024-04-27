from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
from typing import List

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

class Plan(db.Model):
  __tablename__ = "plans"
  id: Mapped[int] = mapped_column(primary_key=True)
  name: Mapped[str] = mapped_column(unique=True)
  price: Mapped[float]
  description: Mapped[str]
  ai_addon: Mapped[bool] = mapped_column(default=False)
  best_value: Mapped[bool] = mapped_column(default=False)
  features: Mapped[List["PlanFeature"]] = relationship()

  def serialize(self):
    return {
      "id": self.id,
      "name": self.name,
      "price": self.price,
      "description": self.description,
      "ai_addon": self.ai_addon,
      "best_value": self.best_value,
      "features": [feature.serialize() for feature in self.features]
    }
  
class PlanFeature(db.Model):
  __tablename__ = "plan_features"
  id: Mapped[int] = mapped_column(primary_key=True)
  plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
  description: Mapped[str]
  hidden: Mapped[bool] = mapped_column(default=False)
  plan: Mapped["Plan"] = relationship("Plan", viewonly=True)

  def serialize(self):
    return {
      "description": self.description,
      "hidden": self.hidden
    }

class Question(db.Model):
  __tablename__ = "questions"
  id: Mapped[int] = mapped_column(primary_key=True)
  question: Mapped[str]
  answer: Mapped[str]

  def serialize(self):
    return {
      "id": self.id,
      "question": self.question,
      "answer": self.answer
    }