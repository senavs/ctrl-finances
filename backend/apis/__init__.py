from flask_restful import Api

from backend.apis.base_resource import BaseResource

api = Api()

# resources
api.add_resource(BaseResource, '/base')
