from socket import *
import threading

class newclient(threading.Thread):
    def __init__(self, addr,connection):
        threading.Thread.__init__(self)
        self.addr = addr
        self.socket = connection
        print "New thread Made\n"
    def run(self):
        print "Connecting to" + str(addr)
	try:
		print 'Working'
		connection.send("HTTP/1.1 200 OK\r\n\r\n")
		message = connection.recv(1024)
		filename = message.split()[1] #cuts off the '/' in the request page
		f = open(filename[1:])
		outputdata = f.read()
		for i in range(0, len(outputdata)):
			connection.send(outputdata[i])
		connection.close()
	except IOError:
		print 'IO ERROR'
		connection.send("404 NOT FOUND")
		connection.close()
	except KeyboardInterrupt:
		server.close()
		connection.close()
		exit();



server = socket(AF_INET, SOCK_STREAM)
port = 12030
server.bind((gethostname(), port))

while True:
    server.listen(5) 
    print 'Ready to serve'
    connection,  addr = server.accept()
    newthread = newclient(addr,connection)
    newthread.start()
#threads set to daemon so no stdin capture
#in browser open page with '"computer_name":12030'
