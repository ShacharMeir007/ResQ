import socket
import select
import json
from Request import *
from RequestDecoder import *
import image_server
from DataBaseManager import *
"""
this is the server.
the server receive request from client send to database and return to client the response.
the server receive data from hospitals and upload to data base.
"""

codes = []

database = DataBaseManager()
def main():
    server_socket = socket.socket()
    server_socket.bind(('0.0.0.0', 1802))
    server_socket.listen()
    open_client_sockets = []
    messages_to_send = []
    while True:
        rlist, wlist, xlist = select.select([server_socket] + open_client_sockets, [mes[0] for mes in messages_to_send],
                                            [])
        for current_socket in rlist:
            if current_socket is server_socket:
                # new client
                (new_socket, address) = server_socket.accept()
                open_client_sockets.append(new_socket)
            else:
                data1 = current_socket.recv(10240)
                data = current_socket.recv(20000)
                previous = ""
                while (len(data) > len(previous)):
                    previous = data
                    data += current_socket.recv(20000)

                if data1 == "":
                    open_client_sockets.remove(current_socket)
                else:
                    request = json.loads(data1, cls=RequestDecoder)
                    if request.command == "search":
                        request.data["image"] = data
                        handle_search(request, messages_to_send, current_socket)
                    elif request.command == "upload":
                        request.data["images"] = data
                        handle_upload(request, messages_to_send, current_socket)



def handle_search(request, messages_to_send, current_socket):
    """
    handle the search for a pic
    :param request: the request received
    :param messages_to_send: the messages needed to be sent
    :param current_socket: the requester
    :return: none
    """
    # todo check if input correct
    f = open("missing.jpg", "wb")  # there will be few files at the same time in the future
    f.write(request.data["image"])
    f.close()
    (name, pr) = image_server.search("missing.jpg")
    if pr > 0.5:  # todo make a function that uses the input known about the face
        status = database.search(name)
        messages_to_send.append((current_socket, "found at " + status.hospital))
    else:
        messages_to_send.append((current_socket, "sorry, we couldn't find the person you are looking for"))



def handle_upload(request, messages_to_send, current_socket):
    """
    handle the uploading of new person to the databases
    """
    f = open("new_person.zip", "wb")
    f.write(request.data["images"].encode(), 2)
    f.close()
    name = (request.data["status"].name if request.data["status"].name != "" else "anon") + "-" + \
           (request.data["status"].id_number if request.data["status"].id_number != "" else genarate_code(codes))
    image_server.upload("new_person.zip", name)
    database.upload(request.data["status"], name)


def genarate_code(l):
    """
    help to create a code for unrecognized person
    """
    n = [i for i in range(10 ** 5, 10 ** 6 - 1)]
    s = list(set(n).difference(set(l)))
    l.append(s[0])
    return s[0]


if __name__ == "__main__":
    main()
