from backend.core.database import db


class StructureBase:
    ID = db.Column(db.Integer, primary_key=True)

    def json(self) -> dict:
        return {'ID': self.ID}

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'{type(self).__name__}({self.ID})'


class QueryBase:

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, id: int):
        return cls.query.get(id)
