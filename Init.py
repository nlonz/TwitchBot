import socket, string, json, urllib2
import Config

def init():
	s = socket.socket()
	s.connect((Config.HOST, Config.PORT))
	s.send("PASS " + Config.PASS + "\r\n")
	s.send("NICK " + Config.NICK + "\r\n")
	s.send("JOIN #" + Config.CHANNEL + "\r\n")
	return s

def sendMessage(s, message):
	message = "PRIVMSG #" + Config.CHANNEL + " :" + message + "\r\n"
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
	
def getSRCId(): 
	url = "http://www.speedrun.com/api/v1/users?name=" + Config.SRCUSER
	print url
	id = json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("data")[0].get("id")
	print id
	Config.SRCID = id
	
def isLoadingComplete(line):
	if("End of /NAMES list" in line):
		return False
	else:
		return True