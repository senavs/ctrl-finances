from flask_restful import Resource

from backend.core.models.account import AccountModel
from backend.core.models.user import UserModel
from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.utils.constants import (SUCCESS_FOUND, ERROR_FOUND, ERROR_ALREADY_REGISTERED, ERROR_FK_FOUND,
                                          SUCCESS_CREATED, SUCCESS_EDITED, SUCCESS_DELETED, ERROR_INVALID_PASSWORD)


class AccountResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/account.json', 'get')
    post_parser = Parser('backend/core/schemas/account.json', 'post')
    put_parser = Parser('backend/core/schemas/account.json', 'put')
    delete_parser = Parser('backend/core/schemas/account.json', 'delete')

    def get(self):
        request = self.get_parser.parse_args()

        if request['nm_account']:
            account = AccountModel.find_by_nm_account(request['nm_account'])

            if not account:
                return self.response.error(**ERROR_FOUND)
            return self.response.success(**SUCCESS_FOUND, account=account.json())
        else:
            accounts = AccountModel.find_all()
            accounts = [account.json() for account in accounts]
            return self.response.success(**SUCCESS_FOUND, accounts=accounts)

    def post(self):
        request = self.post_parser.parse_args()

        account = AccountModel.find_by_nm_account(request['nm_account'])
        if account:
            return self.response.error(**ERROR_ALREADY_REGISTERED)

        user = UserModel.find_by_id(request['id_user'])
        if not user:
            return self.response.error(**ERROR_FK_FOUND, foreign_key='id_user')

        new_account = AccountModel(request['id_user'], request['nm_account'])
        new_account.insert()
        return self.response.success(**SUCCESS_CREATED, account=new_account.json())

    def put(self):
        request = self.put_parser.parse_args()

        account = AccountModel.find_by_nm_account(request['nm_account'])
        if not account:
            return self.response.error(**ERROR_FOUND)

        user = UserModel.find_by_id(request['id_user'])
        if not user:
            return self.response.error(**ERROR_FK_FOUND, foreign_key='id_user')

        account.NM_ACCOUNT = request['new_nm_account']
        account.insert()
        return self.response.success(**SUCCESS_EDITED, account=account.json())

    def delete(self):
        request = self.delete_parser.parse_args()

        account = AccountModel.find_by_nm_account(request['nm_account'])
        if not account:
            return self.response.error(**ERROR_FOUND)

        account.delete()
        return self.response.success(**SUCCESS_DELETED)
