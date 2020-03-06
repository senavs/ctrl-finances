def set_error(err):
    """Prepare ErrorHandler methods to Flaks register_error_handler"""

    def decorator(func):
        return err, func

    return decorator


def get_methods(cls):
    """Get all attributes and method of a class (without hidden and magics methods)"""
    return (getattr(cls, attr) for attr in dir(cls) if not attr.startswith('_'))


class ErrorHandler:

    @staticmethod
    @set_error(400)
    def bad_request(e):
        """Error 400, Bad Request"""
        return {'message': 'Bad Request!'}

    @staticmethod
    @set_error(404)
    def not_found(e):
        """Error 404, Not Found"""
        return {'message': 'Page Not Found.'}

    @staticmethod
    @set_error(500)
    def internal(e):
        """Error 500, Internal Server Error"""
        return {'message': 'Internal Server Error.'}
