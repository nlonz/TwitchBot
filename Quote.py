import random

def loadQuotes():
	f = open(r'D:\Dev\EmoArbot\connor75.txt', 'rb')
	quotes = f.readlines()
	f.close()
	return quotes
	
def getQuote(num):
	if 'rand' == num:
		num = str(random.randrange(1,len(quotes)))
	if num.isdigit():
		num = int(num)
		if 0 <= num-1 and num-1 < len(quotes):
			return quotes[num-1]
	return 'FAIL'
	
quotes = loadQuotes()