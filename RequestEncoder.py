import json

from Request import *

from Status import *
from StatusEncoder import *


class RequestEncoder(json.JSONEncoder):
    """An encoder of requests."""
    

    def default(self, o):
        """The default method for the encoding.

        Args:
            self: the encoder.
            o: an object to encode.
        """

        if isinstance(o, Request):
            return {"index": o.index,
                    "command": o.command,
                    "data": o.data}

        elif isinstance(o, Status):
            return json.dumps(o, cls = StatusEncoder)

        else:
            return super().encode(o)
