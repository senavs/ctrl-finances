from flask_restful import Api

from backend.apis.user import UserResource
from backend.apis.account import AccountResource
from backend.apis.movement import MovementResource
from backend.apis.movement_type import MovementTypeResource
from backend.apis.movement_tag import MovementTagResource

api = Api()

# resources
api.add_resource(UserResource, '/user')
api.add_resource(AccountResource, '/account')
api.add_resource(MovementResource, '/movement')
api.add_resource(MovementTypeResource, '/movement_type')
api.add_resource(MovementTagResource, '/movement_tag')
