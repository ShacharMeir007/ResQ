import json

from Request import *

from StatusDecoder import *

class RequestDecoder(json.JSONDecoder):
    """A decoder of requests."""
    

    def decode(self, s):
        """Decode a string to a CRPRequest.
        Args:
            self: the decoder.
            s: a string to decode.

        """

        as_dictionary = super().decode(s)

        # Decode the dictionary.
        if as_dictionary["command"] == "upload":
            data_dict = {"status": json.loads(as_dictionary["data"]["status"]), "images": as_dictionary["data"]["images"]}

        elif as_dictionary["command"] == "search":
            data_dict = as_dictionary["data"]

        else:
            raise AttributeError()
        
        return Request(as_dictionary['index'], as_dictionary['command'], data_dict)
