from socket import *
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
print ('Client X: Alice')
message = 'Client X: Alice'
clientSocket.send(message.encode())
reply = clientSocket.recv(1024)
print('From Server:',reply.decode())
clientSocket.close()





    #def clienthandler():
    #connectionSocket, addr = clientSocket.accept()
    #print (addr, "Client X: Alice")
    #while 1:
    #   message = connectionSocket.recv(1024)
    #   if not message:
#       break

#for i in range(5):
#   Thread(target=clienthandler).start()



