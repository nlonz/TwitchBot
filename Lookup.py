import json
import urllib2
import Config
from Dicts import categories
from Enum import Month

recordBaseUrl = "http://www.speedrun.com/api/v1/categories/"
personalBests = {}

def populatePersonalBests(username):
	url = "http://www.speedrun.com/api/v1/users?name=" + Config.SRCUSER
	srcid = json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("data")[0].get("id")
	pbUrl = "http://www.speedrun.com/api/v1/users/" + srcid + "/personal-bests"
	global personalBests
	personalBests = json.loads(urllib2.urlopen(pbUrl).read().decode("utf-8")).get("data")

def fetchWRs():
	wrs = {}
	for category in categories:
		categoryCode = categories.get(category, "Not found")
		if ("Not found" == categoryCode):	
			return "The world record for this category is not posted on speedrun.com, or I don't know about this category."
		else:
			recordUrl = recordBaseUrl + categoryCode + "/records"
			run = json.loads(urllib2.urlopen(recordUrl).read().decode("utf-8")).get("data")[0].get("runs")[0].get("run")
			wrs[category] = "The world record is " + parseTime(run.get("times").get("realtime")) + " done by " + getUsernameFromId(run) + " on " + parseDate(run.get("date"))
	return wrs
	
def lookUpPB(category):
	categoryCode = categories.get(category, "Not found")
	if("Not found" == categoryCode):
		return "My personal best is not posted on speedrun.com"
	for run in personalBests:
		if (categories[category] == run.get("run").get("category")):
			return "My personal best is " + parseTime(run.get("run").get("times").get("realtime")) + " done on " + parseDate(run.get("run").get("submitted")) + " and is currently " + getPosition(run) + " place on the leaderboards"
	
def lookUpWR(category):
	return worldRecords[category]
		
def getUsernameFromId(run):
	userId = run.get("players")[0].get("id")
	userNameUrl = "http://www.speedrun.com/api/v1/users/" + userId
	userName = json.loads(urllib2.urlopen(userNameUrl).read().decode("utf-8")).get("data").get("names").get("international")
	return userName

def parseTime(time):
	parsedTime = ""
	if 'H' in time:
		parsedTime = time[time.index('T')+1:time.index('H')] + ":"
	parsedTime += getMinutes(time)
	parsedTime += getSeconds(time)
	return parsedTime
	
def getMinutes(time):
	if 'M' not in time:
		return "00"
	else:
		if 'H' in time:
			minutes = time[time.index('H')+1:time.index('M')]
		else:
			minutes = time[time.index('T')+1:time.index('M')]
		if 10 > int(minutes):
			minutes = "0" + minutes
		return minutes + ":"
	
def getSeconds(time):
	if 'S' not in time:
		return "00"
	else:
		if 'H' in time and 'M' not in time:
			seconds = time[time.index('H')+1:time.index("S")]
		elif 'M' in time:
			seconds = time[time.index('M')+1:time.index('S')]
		else:
			seconds = time[time.index('T')+1:time.index('S')]	
		if 10 > float(seconds):
			seconds = "0" + seconds
		return seconds

def parseDate(time):
	year = time[0:4]
	month = time[5:7]
	day = time[8:10]
	return Month.reverse_mapping[int(month)] + " " + day + ", " + year
	
def getPosition(run):
	position = str(run.get("place"))
	if position.endswith("1") and not position.endswith("11"):
		suffix = "st"
	elif position.endswith("2") and not position.endswith("12"):
		suffix = "nd"
	elif position.endswith("3") and not position.endswith("13"):
		suffix = "rd"
	else:
		suffix = "th"
	return position + suffix

worldRecords = fetchWRs()
populatePersonalBests(Config.SRCUSER)