from socket import *

server = socket(AF_INET, SOCK_STREAM)
port = 12030
server.bind((gethostname(), port))
server.listen(5)
while True:
    print 'Ready to serve'
    conection,  addr = server.accept()
    try:
        print 'Working'
        conection.close()
    except IOError:
        print 'Something happened kinda badly'
        connection.close()
        server.close()
