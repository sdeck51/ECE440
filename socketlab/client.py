import socket
import sys

# Create a TCP/IP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1], sys.argv[2])
client.connect(server_address)

while True:
	print "Ready..."
	try:
		target = sys.argv[3]
		s.send(target)
	finally:
		client.close()
