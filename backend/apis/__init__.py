from flask_restful import Api

from backend.apis.movement_type import MovementResource

api = Api()

# resources
api.add_resource(MovementResource, '/movement_type')
