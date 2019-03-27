from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
ClientX = 'Client X: Alice'
print (ClientX)
message = input('Enter the name')
clientSocket.send(ClientX.encode())
reply = clientSocket.recv(1024)
print('From Server:', reply.decode())
clientSocket.close()
