from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .. import db
from .plan_model import Plan

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