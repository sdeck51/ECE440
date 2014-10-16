from socket import *
server = socket(AF_INET, SOCK_STREAM)
port = 12030
server.bind((gethostname(), port))
server.listen(1)
while True:
    print 'Ready to serve'
    connection,  addr = server.accept()
    try:
		print 'Working'
		print 'Working'
		connection.send('''HTTP/1.1 200 OK
Content-Type: text/html

''')
		message = connection.recv(1024)
		print message
		filename = message.split()[1] #cuts off the '/' in the request page
		f = open(filename[1:])
		outputdata = f.read()
		for i in range(0, len(outputdata)):
			connection.send(outputdata[i])
		connection.close()
    except IOError:
		print 'IO ERROR'
		connection.send("404 NOT FOUND")
		print message
		connection.close()
    except KeyboardInterrupt:
        server.close()
        connection.close()
        break;


#threads set to daemon so no stdin capture
#in browser open page with '"computer_name":12030'
