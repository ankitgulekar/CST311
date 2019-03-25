from socket import *
from threading import Thread
serverName = localhost
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

for i in range(2):
  Thread(target=clientHandler).start()


def clientHandler():
    connectionSocket, addr = clientSocket.accept()
    print (addr, "Client Y")
    while 1:
        message = connectionSocket.recv(1024)
        if not message:
            break
        

 clientSocket.close()
