from socket import *
import thread

BUFF = 1024
HOST = '127.0.0.1'  # must be input parameter @TODO
PORT = 12000  # must be input parameter @TODO

counter = 0
clientY = "Client Y: Bob"
yCount = 0
clientX = "Client X: Alice"
xCount = 0
first = ""


def response(key):
    return key


def handler(clientsock, addr):
    global counter
    global clientY
    global clientX
    global first
    global xCount
    global yCount

    while 1:
        try:
            data = clientsock.recv(BUFF)
            if not data: break
            print '---------------------------\n'
            print '[DATA]'
            print data
            print '[FIRST]'
            print first
            print '[COUNTER]'
            print counter
            print '---------------------------\n'


            # if client y connected increase counter
            # if a first client name hasn't been established set it
            if data == clientY:
                if first == "":
                    first = clientY
                if yCount == 0:
                    counter = counter + 1
                    yCount = yCount + 1

            elif data == clientX:
                if first == "":
                    first = clientX
                if xCount == 0:
                    xCount = xCount + 1
                    counter = counter + 1

            print '---------------------------\n'
            print '[DATA]'
            print data
            print '[FIRST]'
            print first
            print '[COUNTER]'
            print counter
            print '---------------------------\n'

            if counter == 2:
                # counter = 0
                # yCount = 0
                # xCount = 0
                if first == clientX:
                    message = "X: Alice received before Y: Bob"
                else:
                    message = "Y: Bob received before X: Alice"
                # first = ""
                clientsock.send(response(message))
                print addr, "- closed connection"  # log on console
                clientsock.close()
                break

        except ValueError:
            print 'something went wront'


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
