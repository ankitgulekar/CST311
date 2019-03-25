from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept()
    sentence = connectionSocket.recv(1024).decode()
    if(sentence == "Client X: Alice"):
        Sentence = ("X: Alice received before Y: Bob")
    else:
        Sentence = (Y: Bob received before X: Alice")
    connectionSocket.send(Sentence.encode())
    connectionSocket.close()

