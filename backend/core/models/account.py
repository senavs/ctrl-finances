from backend.core.database import db
from backend.core.models.base import QueryBase, StructureBase


class AccountModel(StructureBase, QueryBase, db.Model):
    __tablename__ = 'ACCOUNT'
    NM_ACCOUNT = db.Column(db.String(128), unique=True, nullable=False)
    ID_USER = db.Column(db.Integer, db.ForeignKey('USER.ID'), nullable=False)

    user = db.relationship("UserModel", backref="ACCOUNT")

    def __init__(self, id_user: int, nm_account: str):
        self.ID_USER = id_user
        self.NM_ACCOUNT = nm_account

    def json(self) -> dict:
        return {'ID': self.ID, 'ID_USER': self.ID_USER, 'NM_ACCOUNT': self.NM_ACCOUNT, 'USER': self.user.json()}

    @classmethod
    def find_by_nm_account(cls, nm_account: str) -> 'AccountModel':
        return cls.query.filter_by(NM_ACCOUNT=nm_account).first()
