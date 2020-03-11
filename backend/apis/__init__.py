from flask_restful import Api

from backend.apis.movement_type import MovementTypeResource
from backend.apis.movement_tag import MovementTagResource

api = Api()

# resources
api.add_resource(MovementTypeResource, '/movement_type')
api.add_resource(MovementTagResource, '/movement_tag')
