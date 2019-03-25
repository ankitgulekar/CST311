from socket import *
from threading import Thread

serverName = localhost
serverPort = 12000
clientSocket = socket ( AF_INET, SOCK_STREAM )
clientSocket.connect ( (serverName, serverPort) )
message = 'Client Y: Bob'

for i in range ( 2 ):
    Thread ( target=clienthandler ).start ()


def clienthandler():
    connectionSocket, addr = clientSocket.accept ()
    #print ( addr, "Client Y: Bob" )
    while 1:
        message = connectionSocket.recv ( 1024 )
        if not message:
            break


clientSocket.close ()
