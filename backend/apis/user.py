from flask_restful import Resource

from backend.core.models.user import UserModel
from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.utils.constants import (SUCCESS_FOUND, ERROR_FOUND, ERROR_ALREADY_REGISTERED,
                                          SUCCESS_CREATED, SUCCESS_EDITED, SUCCESS_DELETED, ERROR_INVALID_PASSWORD)


class UserResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/user.json', 'get')
    post_parser = Parser('backend/core/schemas/user.json', 'post')
    put_parser = Parser('backend/core/schemas/user.json', 'put')
    delete_parser = Parser('backend/core/schemas/user.json', 'delete')

    def get(self):
        request = self.get_parser.parse_args()

        if request['nm_username']:
            user = UserModel.find_by_nm_username(request['nm_username'])

            if not user:
                return self.response.error(**ERROR_FOUND)
            return self.response.success(**SUCCESS_FOUND, user=user.json())
        else:
            users = UserModel.find_all()
            users = [user.json() for user in users]
            return self.response.success(**SUCCESS_FOUND, users=users)

    def post(self):
        request = self.post_parser.parse_args()

        user = UserModel.find_by_nm_username(request['nm_username'])
        if user:
            return self.response.error(**ERROR_ALREADY_REGISTERED)

        new_user = UserModel(request['nm_username'], request['nm_password'])
        new_user.insert()
        return self.response.success(**SUCCESS_CREATED, user=new_user.json())

    def put(self):
        request = self.put_parser.parse_args()

        user = UserModel.find_by_nm_username(request['nm_username'])
        if not user:
            return self.response.error(**ERROR_FOUND)

        if not user.check_password(request['nm_password']):
            return self.response.error(**ERROR_INVALID_PASSWORD)

        user.change_password(request['new_nm_password'])
        user.insert()
        return self.response.success(**SUCCESS_EDITED, user=user.json())

    def delete(self):
        request = self.delete_parser.parse_args()

        user = UserModel.find_by_nm_username(request['nm_username'])
        if not user:
            return self.response.error(**ERROR_FOUND)

        user.delete()
        return self.response.success(**SUCCESS_DELETED)
