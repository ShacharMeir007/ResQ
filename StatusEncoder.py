import json

from Status import *


class StatusEncoder(json.JSONEncoder):
    """An encoder of status.
    """
    

    def default(self, o):
        """The default method for the encoding.
        Args:
            self: the encoder.
            o: an object to encode.
        """

        if isinstance(o, Status):
            return {"chance": o.chance,
                    "hospial": o.hospital,
                    "id_number": o.id_number,
                    "name": o.name}
        else:
            return super().encode(o)
