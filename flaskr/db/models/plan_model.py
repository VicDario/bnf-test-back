from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from .. import db
from .plan_feature_model import PlanFeature

class Plan(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(unique=True)
    price: Mapped[float]
    features: Mapped[List["PlanFeature"]] = mapped_column(back_populates="plan")