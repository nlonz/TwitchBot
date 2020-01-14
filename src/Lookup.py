import json
import urllib2
import Config
from Categories import categories
from Enum import Month

recordBaseUrl = "http://www.speedrun.com/api/v1/categories/"
personalBests = {}


def populate_personal_bests():
    url = "http://www.speedrun.com/api/v1/users?name=emoarbiter"
    srcid = json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("data")[0].get("id")
    pb_url = "http://www.speedrun.com/api/v1/users/" + srcid + "/personal-bests"
    global personalBests
    personalBests = json.loads(urllib2.urlopen(pb_url).read().decode("utf-8")).get("data")


def fetch_records():
    wrs = {}
    for category in categories:
        category_code = categories.get(category, "Not found")
        if "Not found" == category_code:
            return "The world record for this category is not posted on speedrun.com, or I don't know about this category."
        else:
            record_url = recordBaseUrl + category_code + "/records"
            run = json.loads(urllib2.urlopen(record_url).read().decode("utf-8")).get("data")[0] .get("runs")[0].get("run")
            wrs[category] = "The world record is " + parse_time(
                run.get("times").get("realtime")) + " done by " + get_username_from_id(run) + " on " + parse_date(
                run.get("date"))
    return wrs


def look_up_pb(category):
    category_code = categories.get(category, "Not found")
    if "Not found" == category_code:
        return "My personal best is not posted on speedrun.com"
    for run in personalBests:
        if categories[category] == run.get("run").get("category"):
            return "My personal best is " + parse_time(
                run.get("run").get("times").get("realtime")) + " done on " + parse_date(run.get("run").get("submitted")) + " and is currently " + get_position(run) + " place on the leaderboards"


def look_up_wr(category):
    return worldRecords[category]


def get_username_from_id(run):
    user_id = run.get("players")[0].get("id")
    user_name_url = "http://www.speedrun.com/api/v1/users/" + user_id
    user_name = json.loads(urllib2.urlopen(user_name_url).read().decode("utf-8")).get("data").get("names").get("international")
    return user_name


def parse_time(time):
    parsed_time = ""
    if 'H' in time:
        parsed_time = time[time.index('T') + 1:time.index('H')] + ":"
    parsed_time += get_minutes(time)
    parsed_time += get_seconds(time)
    return parsed_time


def get_minutes(time):
    if 'M' not in time:
        return "00"
    else:
        if 'H' in time:
            minutes = time[time.index('H') + 1:time.index('M')]
        else:
            minutes = time[time.index('T') + 1:time.index('M')]
        if 10 > int(minutes):
            minutes = "0" + minutes
        return minutes + ":"


def get_seconds(time):
    if 'S' not in time:
        return "00"
    else:
        if 'H' in time and 'M' not in time:
            seconds = time[time.index('H') + 1:time.index("S")]
        elif 'M' in time:
            seconds = time[time.index('M') + 1:time.index('S')]
        else:
            seconds = time[time.index('T') + 1:time.index('S')]
        if 10.0 > float(seconds):
            seconds = "0" + seconds
        return seconds


def parse_date(time):
    year = time[0:4]
    month = time[5:7]
    day = time[8:10]
    return Month.reverse_mapping[int(month)] + " " + day + ", " + year


def get_position(run):
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


if Config.CHANNEL == "EmoArbiter":
    print("mornin")
    worldRecords = fetch_records()
    populate_personal_bests()
