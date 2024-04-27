from sqlalchemy.orm import Mapped, mapped_column

from .. import db

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