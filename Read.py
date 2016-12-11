import string

def getUsername(line):
	return string.split(string.split(line, ":")[1], "!")[0]
	
def getMessage(line):
	message = string.split(line, ":")[2]
	return message[:len(message)-1]