[2;2Rnt.py
#to run this program use python3 client.py X
#                    or  python3 client.py Y
import threading
from socket import *
import sys
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname

#we are using system variables to determine what client is running at each instant
#client X or client Y
if(len(sys.argv) != 2):
	print("Error. not enough arguments")
	print("\ttry python3 client.py X or python3 client.py Y")
	sys.exit()
if not (sys.argv[1].capitalize() == "X" or sys.argv[1].capitalize() == "Y"):
	print("Error.\ttry python3 client.py X or python3 client.py Y")
	sys.exit()

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect(('',serverPort))
message = input('Enter your name:')
#the message format is  Client X: name entered by the user
message = "Client " + str(sys.argv[1]).capitalize() + ": " + message
clientSocket.send(message.encode())
serverAck = clientSocket.recv(1024)
print ('From Server:', serverAck.decode())
clientSocket.close()
