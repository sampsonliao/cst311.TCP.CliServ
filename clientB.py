import threading
from socket import *
from queue import Queue
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname
serverName = 'localhost'
serverPortB = 13000
clientSocketB = socket(AF_INET, SOCK_STREAM)
clientSocketB.connect((serverName,serverPortB))
message = input('Enter name of client followed by your name:')
clientSocketB.send(message.encode())
serverAck = clientSocketB.recv(1024)
print ('From Server:', serverAck.decode())
clientSocketB.close()
