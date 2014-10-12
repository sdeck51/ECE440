from socket import *
quit = "q"
server = socket(AF_INET, SOCK_STREAM)
port = 12030
server.bind((gethostname(), port))
server.listen(5)
while True:
    print 'Ready to serve'
    conection,  addr = server.accept()
    try:
        print 'Working'
        message = conection.recv(1024)
        filename = message.split()[1]
        f = open(filename[1:])
        close(filename[1:])
        print filename
        conection.close()
    except IOError:
        print 'Something happened kinda badly'
        connection.close()
        server.close()
    except KeyboardInterrupt:
        break;


#threads set to daemon so no stdin capture
#in browser open page with '"computer_name":12030'
