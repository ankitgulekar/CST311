from socket import *
from threading import Thread

serversocket = socket(AF_INET, SOCK_STREAM)
serversocket.bind('localhost', 80)
serversocket.listen(5)


while True:
    # accept connections from outside
    (clientsocket, address) = serversocket.accept()
    # now do something with the clientsocket
    # in this case, we'll pretend this is a threaded server
    ct = client_thread(clientsocket)
    ct.run()

clientSocket.close()
