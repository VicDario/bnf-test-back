from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey

from .. import db
from .plan_model import Plan

class PlanFeature(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    plan_id: Mapped[int] = mapped_column(ForeignKey("plans.id"))
    description: Mapped[str]
    plan: Mapped["Plan"] = relationship("Plan", back_populates="plan_feature")