from flask import Flask

from backend import settings
from backend.apis import api
from backend.core.database import db
from backend.core.handler.errorhandler import ErrorHandler, get_methods

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS

api.init_app(app)
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()


for error in get_methods(ErrorHandler):
    app.register_error_handler(*error)
