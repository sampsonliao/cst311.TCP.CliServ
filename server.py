#TCPCapitalizationServer.py
import threading
import time
from queue import Queue
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
	messageLogger(msg)
	with cv:
		while len(clients) < 2:
			cv.wait()
		cv.notify()
	ack = joinMessage.join(clients).encode()
	connectionSocket.sendto(ack, addr)
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

print("Terminating...")
