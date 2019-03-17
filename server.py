#TCPCapitalizationServer.py
import threading
import time
from queue import Queue
from socket import *

serverPortA = 12000
serverPortB = 13000

clients = []
joinMessage = " received before "

# Create a TCP socket
# Notice the use of SOCK_STREAM for TCP packets

def messageLogger(msg):
	time.sleep(0.5)
	with log_lock:
		print("acquired lock")
		clients.append(msg)
	print("release lock")


def connectionA():
	serverSocket = socket(AF_INET,SOCK_STREAM)
	# Assign IP address and port number to socket
	serverSocket.bind(('',serverPortA))
	serverSocket.listen(1)
	print ('[Connection A]: The server is ready to receive')
	while True:
		connectionSocket, addr = serverSocket.accept()
		message, address = connectionSocket.recvfrom(1024)
		msg = message.decode()
		messageLogger(msg)
		with cv:
			while len(clients) < 2:
				cv.wait()
			cv.notify()
		ack = joinMessage.join(clients)
		connectionSocket.sendto(ack.encode(), address)
		connectionSocket.close()
	

def connectionB():
	serverSocket = socket(AF_INET,SOCK_STREAM)
	# Assign IP address and port number to socket
	serverSocket.bind(('',serverPortB))
	serverSocket.listen(1)
	print ('[Connection B]: The server is ready to receive')
	while True:
		connectionSocket, addr = serverSocket.accept()
		message, address = connectionSocket.recvfrom(1024)
		msg = message.decode()
		messageLogger(msg)
		with cv:
			while len(clients) < 2:
				cv.wait()
			cv.notify()
		ack = joinMessage.join(clients)
		connectionSocket.sendto(ack.encode(), address)
		connectionSocket.close()
	



def connection(serverPort):
	serverSocket = socket(AF_INET,SOCK_STREAM)
	# Assign IP address and port number to socket
	serverSocket.bind(('',serverPort))
	serverSocket.listen(1)
	print ('The server is ready to receive')
	while True:
		connectionSocket, addr = serverSocket.accept()
		message, address = connectionSocket.recvfrom(1024)
		msg = message.decode()
		messageLogger(msg)
		with cv:
			while len(clients) < 2:
				cv.wait()
			cv.notify()
		ack = joinMessage.join(clients)
		connectionSocket.sendto(ack.encode(), address)
		connectionSocket.close()
	
log_lock = threading.Lock()
cv = threading.Condition()

connAThread = threading.Thread(target=connection, args=(serverPortA,), daemon=True)
connBThread = threading.Thread(target=connection, args=(serverPortB,), daemon=True)
connAThread.start()
connBThread.start()
connAthread.join()
connBthread.join()

print("Terminating...")
