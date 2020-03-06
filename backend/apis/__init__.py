from flask_restful import Api

from backend.apis.base_resource import BaseResource
from backend.apis.payment_type.payment_type import PaymentTypeResource
from backend.apis.movement.movement import MovementResource

api = Api()

# resources
api.add_resource(BaseResource, '/base')
api.add_resource(PaymentTypeResource, '/payment_type')
api.add_resource(MovementResource, '/movement')
