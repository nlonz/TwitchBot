import urllib2, json, datetime
from Config import CHANNEL
from Gamble import write_point_totals, retrieve_point_totals

added = False


def get_user_list():
    try:
        url = "http://tmi.twitch.tv/group/user/" + CHANNEL + "/chatters"
        return json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("chatters")
    except urllib2.HTTPError as err:
        if err.code == 503:
            get_user_list()


def update_totals(user, point_totals):
    points = point_totals.get(user.upper(), 0)
    point_totals[user.upper()] = (points + 5)


def add_loyalty():
    point_totals = retrieve_point_totals()
    all_users = get_user_list()

    if all_users is not None:
        for user in all_users.get("moderators"):
            update_totals(str(user), point_totals)

        for user in all_users.get("staff"):
            update_totals(str(user), point_totals)

        for user in all_users.get("admins"):
            update_totals(str(user), point_totals)

        for user in all_users.get("global_mods"):
            update_totals(str(user), point_totals)

        for user in all_users.get("viewers"):
            update_totals(str(user), point_totals)

        write_point_totals(point_totals)

    else:
        add_loyalty()


def add_loyalty_for_user(user):
    point_totals = retrieve_point_totals()
    points = point_totals[user.upper()]
    points += 5
    point_totals[user.upper()] = points
    write_point_totals(point_totals)


while True:
    currentTime = datetime.datetime.now()
    if 0 == currentTime.second and not added:
        add_loyalty()
        added = True
    else:
        added = False
