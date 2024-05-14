#!/usr/bin/env python3
from req_resp import GenericRequest

class Defaults():
    DEFAULT_NAME    = "Generic"
    LOCALHOST       = '0.0.0.0'
    PORT            = 10000
    BUFFER_SIZE     = 1000

    """ Example Callback """
    REQUEST = GenericRequest("Default Function", {"arg1": "default"})  
    @staticmethod
    def default_callback(request: GenericRequest):
        return print(
            f"{request.function} called with {request.args} args"
        )
    """ ############### """