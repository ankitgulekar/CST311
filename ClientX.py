from socket import *
from threading import Thread
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = 'Client X: Alice'
for i in range(5):
    Thread(target=clienthandler).start()


def clienthandler():
    connectionSocket, addr = clientSocket.accept()
    #print (addr, "Client X: Alice")
    while 1:
        message = connectionSocket.recv(1024)
        if not message:
            break
