from datetime import datetime

from backend.core.database import db
from backend.core.models.base import StructureBase, QueryBase


class MovementModel(StructureBase, QueryBase, db.Model):
    DT_MOVEMENT = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    VL_MOVEMENT = db.Column(db.Float, unique=False, nullable=False)
    IN_MOVEMENT = db.Column(db.Boolean, unique=False, nullable=False, default=False)

    def __init__(self, vl_movement: float, in_movement: bool):
        self.VL_MOVEMENT = vl_movement
        self.IN_MOVEMENT = in_movement

    def json(self) -> dict:
        return {'ID': self.ID, 'DT_MOVEMENT': self.DT_MOVEMENT.strftime("%d/%m/%Y"),
                'VL_MOVEMENT': self.VL_MOVEMENT, 'IN_MOVEMENT': self.IN_MOVEMENT}
