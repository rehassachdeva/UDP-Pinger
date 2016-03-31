import time
import sys
from socket import *

# Check command line arguments
if len(sys.argv) != 3:
    print "Usage: python UDPPingerClient <server ip address> <server port no>"
    sys.exit()
    
# Create a UDP socket
# Notice the use of SOCK_DGRAM for UDP packets
clientSocket = socket(AF_INET, SOCK_DGRAM)

# To set waiting time of one second for reponse from server
clientSocket.settimeout(1)

# Declare server's socket address
remoteAddr = (sys.argv[1], int(sys.argv[2]))

# Ping ten times
for i in range(10):
    
    sendTime = time.time()
    message = 'PING ' + str(i + 1) + " " + str(time.strftime("%H:%M:%S"))
    clientSocket.sendto(message, remoteAddr)
    
    try:
        data, server = clientSocket.recvfrom(1024)
        recdTime = time.time()
        rtt = recdTime - sendTime
        print "Message Received", data
        print "Round Trip Time", rtt
        print
    
    except timeout:
        print 'REQUEST TIMED OUT'
        print
