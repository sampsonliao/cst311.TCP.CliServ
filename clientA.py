import threading
from socket import *
from queue import Queue
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname
serverName = 'localhost'
serverPortA = 12000
clientSocketA = socket(AF_INET, SOCK_STREAM)
clientSocketA.connect((serverName,serverPortA))
message = input('Enter your name:')
clientSocketA.send(("Client A:" + message).encode())
serverAck = clientSocketA.recv(1024)
print ('From Server:', serverAck.decode())
clientSocketA.close()
