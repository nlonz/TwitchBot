import socket, string
from Init import init, joinRoom, sendMessage
from Commands import executeCommand

def run():
	openSocket = init()
	joinRoom(openSocket)
	readbuffer = ""

	while True:
		readbuffer = readbuffer + openSocket.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()

		for line in temp:
			if "PING" in line:
				openSocket.send("PONG\r\n")
				break
			
			else:
				result = executeCommand(line)
				if "No message" != result:
					print result
					sendMessage(openSocket, result)
					
run()					