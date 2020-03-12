from typing import List
from datetime import datetime

from backend.core.database import db
from backend.core.models.base import QueryBase, StructureBase


class MovementModel(StructureBase, QueryBase, db.Model):
    __tablename__ = 'MOVEMENT'
    VL_MOVEMENT = db.Column(db.Float, unique=False, nullable=False)
    DT_MOVEMENT = db.Column(db.DateTime, unique=False, nullable=False, default=datetime.utcnow)
    ID_ACCOUNT = db.Column(db.Integer, db.ForeignKey('ACCOUNT.ID'), unique=False, nullable=False)
    ID_MOVEMENT_TYPE = db.Column(db.Integer, db.ForeignKey('MOVEMENT_TYPE.ID'), nullable=False)
    ID_MOVEMENT_TAG = db.Column(db.Integer, db.ForeignKey('MOVEMENT_TAG.ID'), nullable=False)

    account = db.relationship("AccountModel", backref="MOVEMENT")
    movement_type = db.relationship("MovementTypeModel", backref="MOVEMENT")
    movement_tag = db.relationship("MovementTagModel", backref="MOVEMENT")

    def __init__(self, id_account: int, vl_movement: float, id_movement_type: str, id_movement_tag: str):
        self.ID_ACCOUNT = id_account
        self.VL_MOVEMENT = vl_movement
        self.ID_MOVEMENT_TYPE = id_movement_type
        self.ID_MOVEMENT_TAG = id_movement_tag

    @classmethod
    def find_by_id_account(cls, id_account: int) -> List['MovementModel']:
        return cls.query.filter_by(ID_ACCOUNT=id_account).all()

    @classmethod
    def find_last_by_id_account(cls, id_account: int) -> 'MovementModel':
        return cls.query.filter_by(ID_ACCOUNT=id_account).order_by(cls.ID.desc()).first()

    def json(self) -> dict:
        return {'ID': self.ID,
                'VL_MOVEMENT': self.VL_MOVEMENT,
                'DT_MOVEMENT': self.DT_MOVEMENT.strftime('%d/%m/%Y'),
                'ID_ACCOUNT': self.ID_ACCOUNT,
                'ID_MOVEMENT_TYPE': self.ID_MOVEMENT_TYPE,
                'ID_MOVEMENT_TAG': self.ID_MOVEMENT_TAG,
                'ACCOUNT': self.account.json(),
                'MOVEMENT_TYPE': self.movement_type.json(),
                'MOVEMENT_TAG': self.movement_tag.json()}
