import sys
import socket
from Status import *
from Request import *
import json
from RequestEncoder import *
"""
this is a code for client that search for information
in advance versions it will be an app for the rescue teams, or a software on the hospital computer.
we will also need to make verification to make sure only the right people will update information.
"""

def main():
    file_name = sys.argv[1]
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", 1802))
    f = open(file_name, "rb")
    read_data = f.read()
    request = Request(0, "search", {})
    f.close()
    m = json.dumps(request, cls=RequestEncoder).encode()
    my_socket.send(m)
    my_socket.send(read_data)
    my_socket.close()


if __name__ == "__main__":
    main()
