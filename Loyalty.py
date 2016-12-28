import urllib2, json, datetime
from Config import CHANNEL
from Gamble import writePointTotals, retrievePointTotals

def getUserList():
	url = "http://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters"
	return json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("chatters")

def updateTotals(user, pointTotals):
	print user
	points = pointTotals.get(user.upper(), 0)
	pointTotals[user.upper()] = (points + 5)
	
def addLoyalty():
	pointTotals = retrievePointTotals()
	allUsers = getUserList()
	
	for user in allUsers.get("moderators"):
		updateTotals(str(user), pointTotals)
		
	for user in allUsers.get("staff"):
		updateTotals(str(user), pointTotals)
		
	for user in allUsers.get("admins"):
		updateTotals(str(user), pointTotals)
		
	for user in allUsers.get("global_mods"):
		updateTotals(str(user), pointTotals)
		
	for user in allUsers.get("viewers"):
		updateTotals(str(user), pointTotals)
		
	writePointTotals(pointTotals)

def addLoyaltyForUser(user):
	pointTotals = retrievePointTotals()
	points = pointTotals[user.upper()]
	points += 5
	pointTotals[user.upper()] = points
	writePointTotals(pointTotals)
	
while True:
	currentTime = datetime.datetime.now()
	added = False
	if 0 == currentTime.second and not added:
		addLoyalty()
		print retrievePointTotals()
		added = True
	else:
		added = False
