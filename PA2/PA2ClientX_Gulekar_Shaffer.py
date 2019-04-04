from socket import *

serverName = 'localhost'
serverPort = 12000

# socket binding
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))

# Data to be printed and sent
ClientX = 'Client X: Alice'
Client_info = 'X: Alice received before Y: Bob'

# Prompt for input
print (ClientX)
message = input('Enter the name: ')

# Send the message from client to server
clientSocket.send(Client_info.encode())

# Wait for the message from server and print once received
reply = clientSocket.recv(1024)
print(reply.decode())
clientSocket.close()
