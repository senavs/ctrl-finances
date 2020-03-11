from backend.core.utils.functions import make_dict

# success messages
SUCCESS_FOUND = make_dict(http_code=200, message='element found successfully')
SUCCESS_CREATED = make_dict(http_code=200, message='element created successfully')
SUCCESS_EDITED = make_dict(http_code=200, message='element edited successfully')
SUCCESS_DELETED = make_dict(http_code=200, message='element deleted successfully')

# error messages
ERROR_FOUND = make_dict(http_code=404, message='element not found')
ERROR_ALREADY_REGISTERED = make_dict(http_code=409, message='element already registered')
