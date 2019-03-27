from socket import *
serverName = 'localhost'
serverPort = 12000

# socket binding
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))


ClientX = 'Client X: Alice'
Client_info = 'X: Alice received before Y: Bob'


print (ClientX)
message = input('Enter the name: ')
clientSocket.send(Client_info.encode())
reply = clientSocket.recv(1024)
print(reply.decode())
clientSocket.close()
