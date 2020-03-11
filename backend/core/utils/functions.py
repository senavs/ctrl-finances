import json
from collections import OrderedDict


def json_to_dict(file_path: str) -> dict:
    """Load a .json file and return as python dictionary

    :param file_path: (str) json file path
    :return: (dict) json file as dict
    """

    with open(file_path, 'r') as file:
        return json.load(file, object_hook=OrderedDict)


def make_dict(**kwargs):
    return dict(**kwargs)
