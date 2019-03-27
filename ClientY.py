from socket import *

serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
ClientY = 'Client Y: Bob'
Client_info = 'Y: Bob received before X: Alice'
print (ClientY)
message = input('Enter the name: ')
clientSocket.send(Client_info.encode())
reply = clientSocket.recv(1024)
print(reply.decode())
clientSocket.close()
