# cst311.TCP.CliServ

**Basic Multithreaded TCP Client-Server** 

## User Stories

The following **required** functionality is completed:

- [X] You must use TCP sockets; you will need to establish a connection first, since it is a connection oriented protocol.
- [X] Clients must initiate the connection by sending their messages to the server.
- [X] Server receives messages from both clients and establishes which message it received first.
- [X] Server sends acknowledgements to both clients stating which message was received first.
- [X] The server must accept connections from both clients first before receiving the messages from either client.
- [X] The response string from Server to Clients (X: Alice received before Y: Bob, or Y: Bob received before X: Alice) must be in the order the messages from Client X or Client Y are received and NOT the order in which the clients X and Y connected to the server.
- [X] Your program should print out the messages sent by the client at both the client and server and vice versa for messages sent by the server.
- [X] Execute your programs on your mininet virtual machine.
- [X] At the top of your server code, in a comment explain why you need multithreading to solve this problem.
- [X] Program must be well documented.

## Example Walkthrough

### How to:
**Server:**
```
python3 server.py
```
**Client (X):**
```
python3 client.py X
```

**Client (Y):**
```
python3 client.py Y
```



