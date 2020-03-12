from flask_restful import reqparse

from backend.core.utils.functions import json_to_dict


class Parser:
    type_map = {'str': str, 'int': int, 'float': float, 'bool': bool, 'list': list, 'tuple': tuple}

    def __init__(self, file_path: str, method: str):
        """Create a reqparse.RequestParser object based on json file

        :param file_path: json file path
        :param method: which method used
        """

        self.schema = json_to_dict(file_path)[method]
        self.parser = reqparse.RequestParser()

        for argument in self.schema:
            if 'type' in argument:
                argument['type'] = self.type_map.get(argument['type'], str)
            self.parser.add_argument(**argument)

    def parse_args(self):
        """Parser Args

        :return: reqparse.RequestParser().parser_args()
        """

        return self.parser.parse_args()
