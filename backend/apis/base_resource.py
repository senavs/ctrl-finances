from flask_restful import Resource

from backend.core.utils.parser import Parser
from backend.core.utils.response import Response


class BaseResource(Resource):
    response = Response()

    post_parser = Parser('backend/core/schemas/base.json')
    put_parser = Parser('backend/core/schemas/base.json')
    delete_parser = Parser('backend/core/schemas/base.json')

    def get(self):
        return self.response.success(200, message='BaseResource GET method is OK')

    def post(self):
        request = self.post_parser.parse_args()
        return self.response.success(200, message='BaseResource POST method is OK', request_args=request)

    def put(self):
        request = self.put_parser.parse_args()
        return self.response.success(200, message='BaseResource PUT method is OK', request_args=request)

    def delete(self):
        request = self.delete_parser.parse_args()
        return self.response.success(200, message='BaseResource DELETE method is OK', request_args=request)
