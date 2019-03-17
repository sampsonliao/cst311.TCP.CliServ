from socket import *
# In your command prompt, type in hostname and press enter.
# What comes up is your computer's hostname
serverName = 'localhost'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))
message = input('Enter your name:')
clientSocket.send(("Client A:" + message).encode())
serverAck = clientSocket.recv(1024)
print ('From Server:', serverAck.decode())
clientSocket.close()

