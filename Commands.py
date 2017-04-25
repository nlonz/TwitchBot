import Config, socket
from Categories import categories
from Read import getUsername, getMessage
from Lookup import lookUpPB, lookUpWR
from Gamble import gamble, lookUpPoints, pointName
from Enum import SlotEmotes
from Slots import slots
from Init import sendMessage
from Quote import getQuote

def executeCommand(openSocket, line):
	username = getUsername(line)
	message = getMessage(line)
	print username + ": " + message
	
	if "!301" == message:
		sendMessage(openSocket, "The Rareware 301% Race is a race of Banjo-Kazooie 100%, Banjo-Tooie 100%, and Donkey Kong 64 101% all back to back taking place on January 28, 2017. Find out more about it here: http://bombch.us/Bj_W")
		
	if "!ABOUT" == message.upper():
		sendMessage(openSocket, "I am a bot designed by EmoArbiter for use in his Twitch channel. I am written in Python 2.7 and use the speedrun.com REST API for any leaderboard information. Any suggestions for new features and feedback is welcome!")
	
	if "!COMMANDS" == message.upper():
		sendMessage(openSocket, "Available commands are !301, !about, !commands, !pb, !points, !wr")
		
	#if "!GAMBLE" in message.upper():
	#	return gamble(username, message)
		
	if "!MODE" in message.upper() and Config.CHANNEL.upper() == username.upper():
		parts = message.split()
		category = parts[1]
		if category in categories:
			Config.CATEGORY = parts[1]
	
	if "!PB" in message.upper():
		sendMessage(openSocket, lookUpPB(Config.CATEGORY))
		
	#if "!POINTS" == message.upper():
	#	sendMessage(openSocket, username + " has " + str(lookUpPoints(username)) + pointName + ".")
		
	if "!QUIT" == message.upper() and Config.CHANNEL.upper() == username.upper():
		exit()
		
	if "!QUOTE" in message.upper():
		parts = message.split()
		if 1 == len(parts):
			quote = getQuote('rand')
		else:
			quote = getQuote(parts[1])
		if not 'FAIL' == quote:
			sendMessage(openSocket, quote)
		
	if "!SLOTS" == message.upper():
		result = slots()
		sendMessage(openSocket, "[ " + SlotEmotes.reverse_mapping[int(result[0])] + " ] [ "
			+ SlotEmotes.reverse_mapping[int(result[1])] + " ] [ " + SlotEmotes.reverse_mapping[int(result[2])] + " ]")
		if (result[0] == result[1] and result[1] == result[2]):
			sendMessage(openSocket, "You win")
	
	if "!WR" == message.upper():
		sendMessage(openSocket, lookUpWR(Config.CATEGORY))