from flask_restful import reqparse

from backend.core.utils.functions import json_to_dict


class Parser:
    type_map = {'str': str, 'int': int, 'float': float, 'bool': bool, 'list': list, 'tuple': tuple}

    def __init__(self, file_path: str):
        """Create a reqparse.RequestParser object based on json file

        :param file_path: json file path
        """

        self.schema = json_to_dict(file_path)
        self.parser = reqparse.RequestParser()

        for key, value in self.schema.items():
            if 'type' in value:
                value['type'] = self.type_map.get(value['type'], str)
            self.parser.add_argument(**value)

    def parse_args(self):
        """Parser Args

        :return: reqparse.RequestParser().parser_args()
        """

        return self.parser.parse_args()
