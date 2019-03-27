from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print ('Client Y: Bob')
message = input('Enter the name')
clientSocket.send(message.encode())
reply = clientSocket.recv(1024)
print('From Server:', reply.decode())
clientSocket.close()
