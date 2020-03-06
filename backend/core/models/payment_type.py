from backend.core.database import db
from backend.core.models.base import StructureBase, QueryBase


class PaymentTypeModel(StructureBase, QueryBase, db.Model):
    NM_PAYMENT = db.Column(db.String(128), unique=True, nullable=False)

    def __init__(self, nm_payment):
        self.NM_PAYMENT = nm_payment

    def json(self) -> dict:
        return {'ID': self.ID, 'NM_PAYMENT': self.NM_PAYMENT}

    @classmethod
    def find_by_nm_payment(cls, nm_payment: str) -> 'PaymentTypeModel':
        return cls.query.filter_by(NM_PAYMENT=nm_payment).first()
