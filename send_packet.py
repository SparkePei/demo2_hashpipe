#! /usr/bin/python
import socket
import time
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
addr = ("127.0.0.1",5009)
for i in range(1,10001):
	sock.sendto(str(i), addr)
	print "send %d to local address! "%(i)
	time.sleep(0.00001) #0.000001 sec(100ns) no packets loss
