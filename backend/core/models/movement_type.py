from backend.core.database import db
from backend.core.models.base import QueryBase, StructureBase


class MovementTypeModel(StructureBase, QueryBase, db.Model):
    __tablename__ = 'MOVEMENT_TYPE'
    NM_MOVEMENT_TYPE = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, nm_movement_type: str):
        self.NM_MOVEMENT_TYPE = nm_movement_type

    def json(self) -> dict:
        return {'ID': self.ID, 'NM_MOVEMENT_TYPE': self.NM_MOVEMENT_TYPE}

    @classmethod
    def find_by_nm_movement_type(cls, nm_movement_type: str) -> 'MovementTypeModel':
        return cls.query.filter_by(NM_MOVEMENT_TYPE=nm_movement_type).first()
