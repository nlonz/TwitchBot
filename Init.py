import socket, string, json, urllib2
from Config import HOST, PORT, PASS, NICK, CHANNEL

def init():
	s = socket.socket()
	s.connect((HOST, PORT))
	s.send("PASS " + PASS + "\r\n")
	s.send("NICK " + NICK + "\r\n")
	s.send("JOIN #" + CHANNEL + "\r\n")
	return s

def sendMessage(s, message):
	message = "PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
	s.send(message)
	print("Sent: " + message)

def joinRoom(s):
	readbuffer = ""
	Loading = True
	while Loading:
		readbuffer = readbuffer + s.recv(1024)
		temp = string.split(readbuffer, "\n")
		readbuffer = temp.pop()
		
		for line in temp:
			print(line)
			Loading = isLoadingComplete(line)
	print("Successfully joined chat")
	
def isLoadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True