from flask_restful import Resource

from backend.core.models.movement_type import MovementTypeModel
from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.utils.constants import (SUCCESS_FOUND, ERROR_FOUND, ERROR_ALREADY_REGISTERED,
                                          SUCCESS_CREATED, SUCCESS_EDITED, SUCCESS_DELETED)


class MovementResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/movement_type.json', 'get')
    post_parser = Parser('backend/core/schemas/movement_type.json', 'post')
    put_parser = Parser('backend/core/schemas/movement_type.json', 'put')
    delete_parser = Parser('backend/core/schemas/movement_type.json', 'delete')

    def get(self):
        request = self.get_parser.parse_args()

        if request['id']:
            movement_type = MovementTypeModel.find_by_id(request['id'])

            if not movement_type:
                return self.response.error(**ERROR_FOUND)
            return self.response.success(**SUCCESS_FOUND, movement_type=movement_type.json())
        else:
            movement_types = MovementTypeModel.find_all()
            movement_types = [movement_type.json() for movement_type in movement_types]
            return self.response.success(**SUCCESS_FOUND, movement_types=movement_types)

    def post(self):
        request = self.post_parser.parse_args()

        movement_type = MovementTypeModel.find_by_nm_movement_type(request['nm_movement_type'])
        if movement_type:
            return self.response.error(**ERROR_ALREADY_REGISTERED)

        new_movement_type = MovementTypeModel(request['nm_movement_type'])
        new_movement_type.insert()
        return self.response.success(**SUCCESS_CREATED, movement_type=new_movement_type.json())

    def put(self):
        request = self.put_parser.parse_args()

        movement_type = MovementTypeModel.find_by_id(request['id'])
        if not movement_type:
            return self.response.error(**ERROR_FOUND)

        new_movement_type = MovementTypeModel.find_by_nm_movement_type(request['nm_movement_type'])
        if new_movement_type:
            return self.response.error(**ERROR_ALREADY_REGISTERED)

        movement_type.NM_MOVEMENT_TYPE = request['nm_movement_type']
        movement_type.insert()
        return self.response.success(**SUCCESS_EDITED, request_args=request)

    def delete(self):
        request = self.delete_parser.parse_args()

        movement_type = MovementTypeModel.find_by_id(request['id'])
        if not movement_type:
            return self.response.error(**ERROR_FOUND)

        movement_type.delete()
        return self.response.success(**SUCCESS_DELETED)
