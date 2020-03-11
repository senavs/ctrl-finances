from flask_restful import Resource

from backend.core.models.movement_tag import MovementTagModel
from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.utils.constants import (SUCCESS_FOUND, ERROR_FOUND, ERROR_ALREADY_REGISTERED,
                                          SUCCESS_CREATED, SUCCESS_EDITED, SUCCESS_DELETED)


class MovementTagResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/movement_tag.json', 'get')
    post_parser = Parser('backend/core/schemas/movement_tag.json', 'post')
    put_parser = Parser('backend/core/schemas/movement_tag.json', 'put')
    delete_parser = Parser('backend/core/schemas/movement_tag.json', 'delete')

    def get(self):
        request = self.get_parser.parse_args()

        if request['id']:
            movement_tag = MovementTagModel.find_by_id(request['id'])

            if not movement_tag:
                return self.response.error(**ERROR_FOUND)
            return self.response.success(**SUCCESS_FOUND, movement_tag=movement_tag.json())
        else:
            movement_tags = MovementTagModel.find_all()
            movement_tags = [movement_tag.json() for movement_tag in movement_tags]
            return self.response.success(**SUCCESS_FOUND, movement_tags=movement_tags)

    def post(self):
        request = self.post_parser.parse_args()

        movement_tag = MovementTagModel.find_by_nm_movement_tag(request['nm_movement_tag'])
        if movement_tag:
            return self.response.error(**ERROR_ALREADY_REGISTERED)

        new_movement_tag = MovementTagModel(request['nm_movement_tag'])
        new_movement_tag.insert()
        return self.response.success(**SUCCESS_CREATED, movement_tag=new_movement_tag.json())

    def put(self):
        request = self.put_parser.parse_args()

        movement_tag = MovementTagModel.find_by_id(request['id'])
        if not movement_tag:
            return self.response.error(**ERROR_FOUND)

        new_movement_tag = MovementTagModel.find_by_nm_movement_tag(request['nm_movement_tag'])
        if new_movement_tag:
            return self.response.error(**ERROR_ALREADY_REGISTERED)

        movement_tag.NM_MOVEMENT_TAG = request['nm_movement_tag']
        movement_tag.insert()
        return self.response.success(**SUCCESS_EDITED, movement_tag=movement_tag.json())

    def delete(self):
        request = self.delete_parser.parse_args()

        movement_tag = MovementTagModel.find_by_id(request['id'])
        if not movement_tag:
            return self.response.error(**ERROR_FOUND)

        movement_tag.delete()
        return self.response.success(**SUCCESS_DELETED)
