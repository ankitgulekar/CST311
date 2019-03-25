import time
from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
print ('Client X: Alice')
message = 'Client X: Alice'
while True:
    try:
        clientSocket.send(message.encode())
        time.sleep(2)
    except:
        break
reply = clientSocket.recv(1024)
print(reply.decode())
