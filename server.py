from socket import *
from threading import Thread
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print('The server is ready to receive')
#while True:
def clientmanager():
    connectionSocket, addr = serverSocket.accept()
    while True:
        sentence = connectionSocket.recv ( 1024 ).decode ()
    if(sentence == "Client X: Alice"):
        Sentence = "X: Alice received before Y: Bob"
    else:
        Sentence = "Y: Bob received before X: Alice"
    connectionSocket.send(Sentence.encode())

for i in range(2):
    Thread(target=clientmanager).start()

serverSocket.close()
