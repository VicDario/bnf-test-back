from sqlalchemy.orm import Mapped, mapped_column

from .. import db

class Question(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    question: Mapped[str]
    description: Mapped[str]