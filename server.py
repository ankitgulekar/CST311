from socket import *
import thread
import time

BUFF = 1024
HOST = '127.0.0.1'  # must be input parameter @TODO
PORT = 12000  # must be input parameter @TODO


ClientX = False
ClientY = False
Response_message = " "

def response(key):
    return 'Server response: ' + key


def handler(clientsock, addr):
    while 1:
        data = clientsock.recv(BUFF)
        if not data:
            break
        if not ClientX and not ClientY:
            Response_message = data
        if data == 'Client X: Alice':
            ClientX = True
        else :
            ClientY = True

        while not ClientX or not ClientY:


        print repr(addr) + ' recv:' + repr(data)
        #time.sleep(60)
        clientsock.send(response(data))
        print repr(addr) + ' sent:' + repr(response(data))
        if "close" == data.rstrip(): break  # type 'close' on client console to close connection from the server side

    clientsock.close()
    print addr, "- closed connection"  # log on console


if __name__ == '__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        print 'waiting for connection... listening on port', PORT
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        thread.start_new_thread(handler, (clientsock, addr))
