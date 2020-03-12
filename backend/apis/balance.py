from flask_restful import Resource

from backend.core.models.movement import MovementModel
from backend.core.models.account import AccountModel
from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.utils.constants import SUCCESS_FOUND, ERROR_FOUND


class BalanceResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/balance.json', 'get')

    def get(self):
        request = self.get_parser.parse_args()

        account = AccountModel.find_by_nm_account(request['nm_account'])
        if not account:
            return self.response.error(**ERROR_FOUND)

        movements = MovementModel.find_by_id_account(account.ID)
        if not movements:
            return self.response.error(**ERROR_FOUND)

        balance = 0
        for movement in movements:
            balance += movement.VL_MOVEMENT

        return self.response.success(**SUCCESS_FOUND, account=account.json(), balance=balance)
