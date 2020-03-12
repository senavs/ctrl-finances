class Response:

    @staticmethod
    def success(http_code=200, **kwargs):
        return kwargs, http_code

    @staticmethod
    def error(http_code=400, **kwargs):
        return kwargs, http_code
