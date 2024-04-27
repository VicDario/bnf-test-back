from sqlalchemy.orm import Mapped, mapped_column
from typing import List
from .. import db
from .plan_feature_model import PlanFeature

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