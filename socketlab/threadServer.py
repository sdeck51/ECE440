from socket import *
import threading

class newclient(threading.Thread):
    def __init__(self, addr,conection):
        threading.Thread.__init__(self)
        self.addr = addr
        self.socket = conection
        print "New thread Made\n"
    def run(self):
        print "Connecting to" + str(addr)
	try:
		print 'Working'
		conection.send("HTTP /1.1 200 OK\r\n")
		message = conection.recv(1024)
		filename = message.split()[1] #cuts off the '/' in the request page
		f = open(filename[1:])
		outputdata = f.read()
		for i in range(0, len(outputdata)):
			conection.send(outputdata[i])
		conection.close()
	except IOError:
		print 'IO ERROR'
		conection.send("404 NOT FOUND")
		conection.close()
	except KeyboardInterrupt:
		server.close()
		conection.close()
		exit();



server = socket(AF_INET, SOCK_STREAM)
port = 12030
server.bind((gethostname(), port))

while True:
    server.listen(5) 
    print 'Ready to serve'
    conection,  addr = server.accept()
    newthread = newclient(addr,conection)
    newthread.start()
#threads set to daemon so no stdin capture
#in browser open page with '"computer_name":12030'
