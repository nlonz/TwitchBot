import socket, string, Config, json, urllib2, datetime, time
from Init import init, joinRoom
from Commands import executeCommand
from multiprocessing import Process

def run(username):
	url = "https://api.twitch.tv/kraken/streams/" + username + "?client_id=" + Config.CLIENTID
	stream = json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("stream")
	
	if stream is not None:
		openSocket = init(username)
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
					executeCommand(openSocket, line)	
			time.sleep(0.1)
					
if __name__ == '__main__':
	p1 = Process(target=run, args=("konditioner",))
	p2 = Process(target=run, args=("univin",))
	p1.start()
	p2.start()
	while True:
		currentTime = datetime.datetime.now()
		if 0 == currentTime.second:
			p1.terminate()
			p1 = Process(target=run, args=("konditioner",))
			p1.start()
		time.sleep(0.5)