from flask_restful import Resource

from backend.core.models.movement import MovementModel
from backend.core.models.account import AccountModel
from backend.core.models.movement_type import MovementTypeModel
from backend.core.models.movement_tag import MovementTagModel
from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.utils.constants import (SUCCESS_FOUND, ERROR_FOUND, SUCCESS_CREATED, ERROR_ALREADY_REGISTERED,
                                          SUCCESS_EDITED, SUCCESS_DELETED, ERROR_FK_FOUND)


class MovementResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/movement.json', 'get')
    post_parser = Parser('backend/core/schemas/movement.json', 'post')
    put_parser = Parser('backend/core/schemas/movement.json', 'put')
    delete_parser = Parser('backend/core/schemas/movement.json', 'delete')

    def get(self):
        request = self.get_parser.parse_args()

        if request['id']:
            movement = MovementModel.find_by_id(request['id'])

            if not movement:
                return self.response.error(**ERROR_FOUND)
            return self.response.success(**SUCCESS_FOUND, movement=movement.json())
        else:
            movements = MovementModel.find_all()
            movements = [movement.json() for movement in movements]
            return self.response.success(**SUCCESS_FOUND, movements=movements)

    def post(self):
        request = self.post_parser.parse_args()

        account = AccountModel.find_by_id(request['id_account'])
        if not account:
            return self.response.error(**ERROR_FK_FOUND, foreign_key='id_account')

        movement_type = MovementTypeModel.find_by_id(request['id_movement_type'])
        if not movement_type:
            return self.response.error(**ERROR_FK_FOUND, foreign_key='id_movement_type')

        movement_tag = MovementTagModel.find_by_id(request['id_movement_tag'])
        if not movement_tag:
            return self.response.error(**ERROR_FK_FOUND, foreign_key='id_movement_tag')

        movement = MovementModel(**request)
        movement.insert()
        return self.response.error(**SUCCESS_CREATED, movement=movement.json())

    def put(self):
        request = self.put_parser.parse_args()

        movement = MovementModel.find_by_id(request['id'])
        if not movement:
            return self.response.error(**ERROR_FOUND)

        if request['id_account']:
            if not MovementModel.find_by_id(request['id_account']):
                return self.response.error(**ERROR_FK_FOUND, foreign_key='id_account')
            movement.ID_ACCOUNT = request['id_account']
        if request['vl_movement']:
            movement.VL_MOVEMENT = request['vl_movement']
        if request['id_movement_type']:
            if not MovementModel.find_by_id(request['id_movement_type']):
                return self.response.error(**ERROR_FK_FOUND, foreign_key='id_movement_type')
            movement.ID_MOVEMENT_TYPE = request['id_movement_type']
        if request['id_movement_tag']:
            if not MovementModel.find_by_id(request['id_movement_tag']):
                return self.response.error(**ERROR_FK_FOUND, foreign_key='id_movement_tag')
            movement.ID_MOVEMENT_TAG = request['id_movement_tag']

        movement.insert()
        return self.response.success(**SUCCESS_EDITED, movement=movement.json())

    def delete(self):
        request = self.delete_parser.parse_args()

        movement = MovementModel.find_by_id(request['id'])
        if not movement:
            return self.response.error(**ERROR_FOUND)

        movement.delete()
        return self.response.success(**SUCCESS_DELETED)
