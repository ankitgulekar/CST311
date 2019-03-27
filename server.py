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
    return key


def handler(clientsock, addr):
   global ClientX
   global ClientY
   global Response_message
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

                clientsock.send(response(message))
                print addr, "- closed connection"  # log on console
                clientsock.close()
                break





if __name__ == '__main__':
    ADDR = (HOST, PORT)
    serversock = socket(AF_INET, SOCK_STREAM)
    serversock.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    serversock.bind(ADDR)
    serversock.listen(5)
    while 1:
        clientsock, addr = serversock.accept()
        print '...connected from:', addr
        print 'listening on port', PORT
        thread.start_new_thread(handler, (clientsock, addr))
        print thread.start_new_thread
