from socket import *
import sys
print
# Create a TCP/IP socket
client = socket(AF_INET, SOCK_STREAM)
#Connect the socket to the port on the server given by the caller
server_address = (sys.argv[1],((int)(sys.argv[2])))
client.connect(server_address)
target = "GET " + sys.argv[3]
print "Request: ",target
client.send(target)
indata = client.recv(1024)
if not indata:
    quit()
print "From Server: ", indata
indata = client.recv(2048)
if not indata:
    quit()
print "From Server: ", indata
