from flask_bcrypt import check_password_hash, generate_password_hash

from backend.core.database import db
from backend.core.models.base import QueryBase, StructureBase


class UserModel(StructureBase, QueryBase, db.Model):
    __tablename__ = 'USER'
    NM_USERNAME = db.Column(db.String(128), unique=True, nullable=False)
    NM_PASSWORD = db.Column(db.String(128), unique=False, nullable=False)

    def __init__(self, nm_username: str, nm_password: str):
        self.NM_USERNAME = nm_username
        self.NM_PASSWORD = self.generate_password(nm_password)

    def check_password(self, password):
        return check_password_hash(self.NM_PASSWORD, password)

    @staticmethod
    def generate_password(password):
        return generate_password_hash(password)

    def change_password(self, new_password):
        self.NM_PASSWORD = self.generate_password(new_password)

    def json(self) -> dict:
        return {'ID': self.ID, 'NM_USERNAME': self.NM_USERNAME}

    @classmethod
    def find_by_nm_username(cls, nm_username: str) -> 'UserModel':
        return cls.query.filter_by(NM_USERNAME=nm_username).first()
