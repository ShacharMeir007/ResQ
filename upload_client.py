import sys
import socket
from Request import *
from Status import *
from RequestEncoder import *
import json
"""
this is a code for client that upload new information
in advance versions it will be a website.
"""

def main():
    (chance, hospital, id_name, name, file_name) = tuple([1] + sys.argv[1:])
    print("ppp")
    my_socket = socket.socket()
    my_socket.connect(("127.0.0.1", 1802))
    f = open(file_name, "rb")
    request = Request(0, "upload", {"status": Status(int(chance), hospital, id_name, name)})
    my_socket.send(json.dumps(request, cls=RequestEncoder).encode())
    print("here")
    my_socket.send(f.read())
    print(my_socket.recv(1024))
    f.close()
    print("done")

main()

