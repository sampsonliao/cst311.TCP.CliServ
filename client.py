import threading
from socket import *
from queue import Queue
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname
serverName = 'localhost'
serverName = 'localhost'
serverPortA = 12000
serverPortB = 13000
clientSocketA = socket(AF_INET, SOCK_STREAM)
clientSocketB = socket(AF_INET, SOCK_STREAM)

def clientA():
	clientSocketA.connect((serverName,serverPortA))
	message = input('Enter your name:')
	clientSocketA.send(("Client A:" + message).encode())
	serverAck = clientSocketA.recv(1024)
	print ('From Server:', serverAck.decode())
	clientSocketA.close()

def clientB():
	clientSocketB.connect((serverName,serverPortB))
	message = input('Enter your name:')
	clientSocketB.send(("Client B:" + message).encode())
	serverAck = clientSocketB.recv(1024)
	print ('From Server:', serverAck.decode())
	clientSocketB.close()

def threader():
	while True:
		worker = q.get()
		clientA(worker)

for i in range(2):
	t = threading.Thread(target=thread1, daemon=True)
	t.start()

for worker in range(2):
	q.put(worker)
q.join()
