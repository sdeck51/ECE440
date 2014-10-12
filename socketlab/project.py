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
        message = conection.recv(1024)
        filename = message.split()[1] #cuts off the '/' in the request page
        f = open(filename[1:])
        outputdata = f.read()
        for i in range(0, len(outputdata)):
			conection.send(outputdata[i])
        f.close()
        conection.close()
    except IOError:
        print 'Something happened kinda badly'
        server.close()
    except KeyboardInterrupt:
        server.close()
        conection.close()
        break;


#threads set to daemon so no stdin capture
#in browser open page with '"computer_name":12030'
