from flask_restful import Resource

from backend.core.utils.parser import Parser
from backend.core.utils.response import Response
from backend.core.models.payment_type import PaymentTypeModel


class PaymentTypeResource(Resource):
    response = Response()

    get_parser = Parser('backend/core/schemas/payment_type/payment_type_get.json')
    post_parser = Parser('backend/core/schemas/payment_type/payment_type_post.json')
    put_parser = Parser('backend/core/schemas/payment_type/payment_type_put.json')
    delete_parser = Parser('backend/core/schemas/payment_type/payment_type_delete.json')

    def get(self):
        request = self.get_parser.parse_args()

        if request['nm_payment']:
            payment_type = PaymentTypeModel.find_by_nm_payment(request['nm_payment'])

            if not payment_type:
                return self.response.error(404, message='payment type not found')
            return self.response.success(200, message='payment type found successfully', payment_type=payment_type.json())
        else:
            payment_types = PaymentTypeModel.find_all()
            payment_types = [payment_type.json() for payment_type in payment_types]
            return self.response.success(200, message='payment types found successfully', payment_type=payment_types)

    def post(self):
        request = self.post_parser.parse_args()

        payment_type = PaymentTypeModel.find_by_nm_payment(request['nm_payment'])
        if payment_type:
            return self.response.error(409, message='payment type already registered')

        payment_type = PaymentTypeModel(request['nm_payment'])
        payment_type.insert()
        return self.response.success(200, message='payment type registered successfully', payment_type=payment_type.json())

    def put(self):
        request = self.put_parser.parse_args()

        payment_type = PaymentTypeModel.find_by_nm_payment(request['nm_payment'])
        if not payment_type:
            return self.response.error(404, message='payment type not found')

        new_payment_type = PaymentTypeModel.find_by_nm_payment(request['new_nm_payment'])
        if new_payment_type:
            return self.response.error(409, message='payment type already registered')

        payment_type.NM_PAYMENT = request['new_nm_payment']
        payment_type.insert()
        return self.response.success(200, message='payment type edited successfully', payment_type=payment_type.json())

    def delete(self):
        request = self.delete_parser.parse_args()

        payment_type = PaymentTypeModel.find_by_nm_payment(request['nm_payment'])
        if not payment_type:
            return self.response.error(404, message='payment type not found')

        payment_type.delete()
        return self.response.success(200, message='payment type deleted successfully')
