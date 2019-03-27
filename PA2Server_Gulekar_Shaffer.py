# Names: Ankit Gulekar, Erick Shaffer
"""
Why threading?
In a single threaded application, when a client connects to the server,
the server has to wait for data from the client.In this situation, the server cannot accept
any other requests. The first connection has to complete before the next one can be served.
To prevent this we use multi-threading. It allows threads to run simultaneously. Since they are separate
threads we can connect and send messages simultaneously without any issue.
"""

from socket import *
from operator import xor
import thread

# Host, port, and buffer data
BUFF = 1024
HOST = '127.0.0.1'
PORT = 12000

# ClientX & Y keep track as to whether the clients have connected or not
ClientX = False
ClientY = False

# This is the message to be sent back to both client x and y
Response_message = " "


# This is method that handles each client
def handler(clientsock, addr):
    # These are required to use the variables above
    global ClientX
    global ClientY
    global Response_message

    # Put the clients in a waiting loop until ready to send both message back simultaneously
    while 1:

        # Receive the client data
        data = clientsock.recv(BUFF)
        if not data:
            break

        # If no clients have connected before, we know
        # the first message is the one to be sent to both clients
        if not ClientX and not ClientY:
            Response_message = data

        # Check which client is connecting by inspecting the data
        # Mark that the client has connected
        if data == 'X: Alice received before Y: Bob':
            ClientX = True
        else:
            ClientY = True

        # Checks if both have already connected
        while not ClientX or not ClientY:
            continue

        # Send back the message of who connected first
        clientsock.send(Response_message)

    # We want both message to be sent before resetting the data for the next request
    # This means that both client message have been sent, and it's safe to change the data
    if xor(ClientX, ClientY):
        ClientX = False
        ClientY = False
        Response_message = " "

    # Arbitrarily pick a client to set to false. This will allow the XOR to be true for the second client
    ClientX = False
    clientsock.close()


if __name__ == '__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        clientsock, addr = serversock.accept()
        print
        '...connected from:', addr
        print
        'listening on port', PORT
        thread.start_new_thread(handler, (clientsock, addr))
