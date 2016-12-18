import Config
from Categories import categories
from Read import getUsername, getMessage
from Lookup import lookUpPB, lookUpWR
from Gamble import gamble, lookUpPoints, pointName

def executeCommand(line):
	username = getUsername(line)
	message = getMessage(line)
	print username + ": " + message
	
	if "!301" == message:
		return "The Rareware 301% Race is a race of Banjo-Kazooie 100%, Banjo-Tooie 100%, and Donkey Kong 64 101% all back to back taking place on January 28, 2017. Find out more about it here: http://bombch.us/Bj_W"
		
	if "!ABOUT" == message.upper():
		return openSocket, "I am a bot designed by EmoArbiter for use in his Twitch channel. I am written in Python 2.7 and use the speedrun.com REST API for any leaderboard information. Any suggestions for new features and feedback is welcome!"
	
	if "!COMMANDS" == message.upper():
		return "Available commands are !301, !about, !commands, !gamble, !pb, !points, !wr"
		
	if "!GAMBLE" in message.upper():
		return gamble(username, message)
		
	if "!MODE" in message.upper() and Config.CHANNEL.upper() == username.upper():
		parts = message.split()
		category = parts[1]
		if category in categories:
			Config.CATEGORY = parts[1]
		return "No message"
	
	if "!PB" in message.upper():
		return lookUpPB(Config.CATEGORY)
		
	if "!POINTS" == message.upper():
		return username + " has " + str(lookUpPoints(username)) + pointName + "."
		
	if "!QUIT" == message.upper() and Config.CHANNEL.upper() == username.upper():
		exit()
	
	if "!WR" == message.upper():
		return lookUpWR(Config.CATEGORY)
		
	return "No message"