from socket import *
server = socket(AF_INET, SOCK_STREAM)
port = 12030
server.bind((gethostname(), port))
server.listen(1)
while True:
    print 'Ready to serve'
    conection,  addr = server.accept()
    try:
		print 'Working'
		message = conection.recv(1024)
		filename = message.split()[1] #cuts off the '/' in the request page
		f = open(filename[1:])
		outputdata = f.read()
		print outputdata
		conection.send('HTTP/1.1 200 OK\r\n')
		conection.send("Content-Type:text/html\r\n")
		for i in range(0, len(outputdata)):
			conection.send(outputdata[i])
		conection.close()
    except IOError:
		print 'IO ERROR'
		print outputdata
		conection.close()
    except KeyboardInterrupt:
        server.close()
        conection.close()
        break;


#threads set to daemon so no stdin capture
#in browser open page with '"computer_name":12030'
