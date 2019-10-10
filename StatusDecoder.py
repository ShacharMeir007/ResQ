import json

from Status import *


class StatusDecoder(json.JSONDecoder):
    """ A decoder of status. """
    

    def decode(self, s):
        """Decode a string to a Status.

        Args:
            self: the decoder.
            s: a string to decode.
        """
        as_dictionary = super().decode(s)
        return Status(as_dictionary['chance'], as_dictionary['hospital'], int(as_dictionary['id_number']), as_dictionary['name'])
