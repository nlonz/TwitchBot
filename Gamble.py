import pickle, random
from Config import LOYALTYPATH

pointName = "dragonflies"

def retrievePointTotals():
	file = open(LOYALTYPATH, 'rb')
	pointTotals = pickle.load(file)
	file.close()
	return pointTotals
	
def writePointTotals(pointTotals):
	file = open(LOYALTYPATH, 'wb')
	pickle.dump(pointTotals, file)
	file.close()
	
def gamble(user, message):
	messageStr = str(message.split()[1])
	if messageStr.isdigit():
		amount = int(messageStr)
		pointTotals = retrievePointTotals()
		points = lookUpPoints(user)
		if (amount > points):
			return "You do not have enough " + pointName + "."
		
		roll = random.randrange(0,101)
		if (user.upper() == "CONNOR75" or user.upper() == "MONTANANINJA"):
			roll = random.randrange(0,60)
		
		if (roll < 60):
			points -= amount
			result = user + " rolled a " + str(roll) + " and lost " + str(amount) + " " + pointName + ". " + user + " now has " + str(points) + " " + pointName + "."
			
		elif (roll >= 60 and roll < 99):
			points += amount
			result = user + " rolled a " + str(roll) + " and won " + str(amount) + " " + pointName + ". " + user + " now has " + str(points) + " " + pointName + "."
		
		elif (roll == 99 or roll == 100):
			points += (2*amount)
			result = user + " rolled a " + str(roll) + " and won " + str(amount) + " " + pointName + ". " + user + " now has " + str(points) + " " + pointName + "."
			
		else:
			return "Random broke lul"
		
		pointTotals[user.upper()] = points
		writePointTotals(pointTotals)
		return result
	
	else:
		return "Please use a numerical value for gambling."
	
def lookUpPoints(user):
	key = user.upper()
	return retrievePointTotals().get(key, 0)
		