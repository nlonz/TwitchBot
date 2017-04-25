import urllib2, json, datetime
from Config import CHANNEL
from Gamble import writePointTotals, retrievePointTotals

added = False

def getUserList():
	try:
		url = "http://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters"
		return json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("chatters")
	except urllib2.HTTPError as err:
		if err.code == 503:
			getUserList()

def updateTotals(user, pointTotals):
	points = pointTotals.get(user.upper(), 0)
	pointTotals[user.upper()] = (points + 5)
	
def addLoyalty():
	pointTotals = retrievePointTotals()
	allUsers = getUserList()
	
	if allUsers is not None:
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
		
	else:
		addLoyalty()

def addLoyaltyForUser(user):
	pointTotals = retrievePointTotals()
	points = pointTotals[user.upper()]
	points += 5
	pointTotals[user.upper()] = points
	writePointTotals(pointTotals)
	
while True:
	currentTime = datetime.datetime.now()
	if 0 == currentTime.second and not added:
		addLoyalty()
		added = True
	else:
		added = False
