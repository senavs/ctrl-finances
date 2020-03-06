from flask_restful import Resource

from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.models.movement import MovementModel


class MovementResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/movement/movement_get.json')
    post_parser = Parser('backend/core/schemas/movement/movement_post.json')

    def get(self):
        request = self.get_parser.parse_args()

        if request['id']:
            movement = MovementModel.find_by_id(request['id'])

            if not movement:
                return self.response.error(404, message='movement not found')
            return self.response.success(200, message='movement found successfully', payment_type=movement.json())
        else:
            movements = MovementModel.find_all()
            movements = [movement.json() for movement in movements]
            return self.response.success(200, message='movements found successfully', movements=movements)

    def post(self):
        request = self.post_parser.parse_args()

        movement = MovementModel(**request)
        movement.insert()
        return self.response.success(200, message='movement registered successfully', movement=movement.json())
