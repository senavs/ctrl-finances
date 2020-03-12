from backend.core.database import db
from backend.core.models.base import QueryBase, StructureBase


class MovementTagModel(StructureBase, QueryBase, db.Model):
    __tablename__ = 'MOVEMENT_TAG'
    NM_MOVEMENT_TAG = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, nm_movement_tag: str):
        self.NM_MOVEMENT_TAG = nm_movement_tag

    def json(self) -> dict:
        return {'ID': self.ID, 'NM_MOVEMENT_TAG': self.NM_MOVEMENT_TAG}

    @classmethod
    def find_by_nm_movement_tag(cls, nm_movement_tag: str) -> 'MovementTagModel':
        return cls.query.filter_by(NM_MOVEMENT_TAG=nm_movement_tag).first()
