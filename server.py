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

# Represents a "critical section", requiring a lock to update list of messages as received
def messageLogger(msg):
	with log_lock:
		clients.append(msg)

def connection(serverPort):
	serverSocket.listen(2)
	print ('{} - New connecton opened on port {}, ready to receive'.format(threading.current_thread().name, serverPort))
	connectionSocket, addr = serverSocket.accept()
	message, address = connectionSocket.recvfrom(1024)
	msg = message.decode()
	
	# Remove "Client" from message
	msg = msg[len("client"):].strip()
	messageLogger(msg)
	
	# Use a condition variable to wait for all messages to arrive if first, or signal if second
	with cv:
		while len(clients) < 2:
			cv.wait()
		cv.notify()
		
	# Join messages with "received before"
	ack = joinMessage.join(clients)
	print('{} - ACK to be sent through port {}: {}'.format(threading.current_thread().name, serverPort, ack))
	connectionSocket.sendto(ack.encode(), addr)
	connectionSocket.close()

serverPort = 12000

clients = []
joinMessage = " received before "


log_lock = threading.Lock()
cv = threading.Condition()
serverSocket = socket(AF_INET,SOCK_STREAM)
# Assign IP address and port number to socket
serverSocket.bind(('',serverPort))

# Create two threads with the same server port #
connAThread = threading.Thread(target=connection, args=(serverPort,), daemon=True)
connBThread = threading.Thread(target=connection, args=(serverPort,), daemon=True)
connAThread.start()
connBThread.start()
connAThread.join()
connBThread.join()
print("Sent acknowledgment to both X and Y")
print("Terminating...")
serverSocket.close()
