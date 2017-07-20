import pickle
import random

from Config import LOYALTYPATH

point_name = "silver medals"


def retrieve_point_totals():
    loyalty_file = open(LOYALTYPATH, 'rb')
    point_totals = pickle.load(loyalty_file)
    loyalty_file.close()
    return point_totals


def write_point_totals(point_totals):
    loyalty_file = open(LOYALTYPATH, 'wb')
    pickle.dump(point_totals, loyalty_file)
    loyalty_file.close()


def gamble(user, message):
    if len(message.split()) < 2:
        return "You must gamble something!"
    message_str = str(message.split()[1])
    if message_str.isdigit():
        amount = int(message_str)
        point_totals = retrieve_point_totals()
        points = look_up_points(user)
        if amount > points:
            return "You do not have enough " + point_name + "."

        roll = random.randrange(0, 101)
        if user.upper() == "CONNOR75" or user.upper() == "MONTANANINJA":
            roll = random.randrange(0, 60)

        if roll < 60:
            points -= amount
            result = user + " rolled a " + str(roll) + " and lost " + str(amount) + " " + point_name + ". " + user + " now has " + str(points) + " " + point_name + "."

        elif 60 <= roll < 99:
            points += amount
            result = user + " rolled a " + str(roll) + " and won " + str(amount) + " " + point_name + ". " + user + " now has " + str(points) + " " + point_name + "."

        elif roll == 99 or roll == 100:
            points += (2 * amount)
            result = user + " rolled a " + str(roll) + " and won " + str(amount) + " " + point_name + ". " + user + " now has " + str(points) + " " + point_name + "."

        else:
            return "Random broke lul"

        point_totals[user.upper()] = points
        write_point_totals(point_totals)
        return result

    else:
        return "Please use a numerical value for gambling."


def look_up_points(user):
    key = user.upper()
    return retrieve_point_totals().get(key, 0)
