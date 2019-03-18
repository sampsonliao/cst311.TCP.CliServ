#server.py
#In this program we are using threads because we are receiving two messages
#from two clients. We have to send back an acknolegment of who sent a message
#first. If we did not implement threads this program will not determine who
#sent the first message but instead it would determine who connected first.
import threading
import time
from socket import *

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets

def messageLogger(msg):
	with log_lock:
		clients.append(msg)

def connection(serverPort):
	serverSocket = socket(AF_INET,SOCK_STREAM)
	# Assign IP address and port number to socket
	serverSocket.bind(('',serverPort))
	serverSocket.listen(1)
	print ('The server (port {}) is ready to receive'.format(serverPort))
	connectionSocket, addr = serverSocket.accept()
	message, address = connectionSocket.recvfrom(1024)
	msg = message.decode()
	msg = msg[len("client"):].strip()
	messageLogger(msg)
	with cv:
		while len(clients) < 2:
			cv.wait()
		cv.notify()
	ack = joinMessage.join(clients)
	print('ACK to be sent through port {}: {}'.format(serverPort, ack))
	connectionSocket.sendto(ack.encode(), addr)
	connectionSocket.close()

serverPortA = 12000
serverPortB = 13000

clients = []
joinMessage = " received before "


log_lock = threading.Lock()
cv = threading.Condition()

connAThread = threading.Thread(target=connection, args=(serverPortA,), daemon=True)
connBThread = threading.Thread(target=connection, args=(serverPortB,), daemon=True)
connAThread.start()
connBThread.start()
connAThread.join()
connBThread.join()
print("Sent acknowledgment to both X and Y")
print("Terminating...")
