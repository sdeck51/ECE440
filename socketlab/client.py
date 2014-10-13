from socket import *
import sys

print "This is line 1"
p = (int)(sys.argv[1])
print type(p)
# Create a TCP/IP socket
client = socket(AF_INET, SOCK_STREAM)
#Connect the socket to the port on the server given by the caller
server_address = (gethostname(),((int)(sys.argv[1])))
client.connect(server_address)

while True:
	print "Ready..."
	try:
		target = sys.argv[2]
		client.send(target)
                indata = client.recv(1024)
                print indata
	finally:
		client.close()
