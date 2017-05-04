import Config
from Categories import categories
from Enum import SlotEmotes
from Gamble import gamble, look_up_points, point_name
from Init import send_message
from Lookup import look_up_pb, look_up_wr
from Quote import get_quote
from Read import get_username, get_message
from Slots import slots


def executeCommand(open_socket, line):
    username = get_username(line)
    message = get_message(line)

    if "!301" == message:
        send_message(open_socket, "The Rareware 301% Race is a race of Banjo-Kazooie 100%, Banjo-Tooie 100%, and Donkey Kong 64 101% all back to back taking place on January 28, 2017. Find out more "
                                  "about it here: http://bombch.us/Bj_W")

    if "!ABOUT" == message.upper():
        send_message(open_socket,
                     "I am a bot designed by EmoArbiter for use in his Twitch channel. I am written in Python 2.7 and use the speedrun.com REST API for any leaderboard information. Any suggestions "
                     "for new features and feedback is welcome!")

    if "!COMMANDS" == message.upper():
        send_message(open_socket, "Available commands are !301, !about, !commands, !pb, !points, !w")

    if "!GAMBLE" in message.upper():
        return gamble(username, message)

    if "!MODE" in message.upper() and Config.CHANNEL.upper() == username.upper() and Config.CHANNEL.upper() == Config.USER.upper():
        parts = message.split()
        category = parts[1]
        if category in categories:
            Config.CATEGORY = parts[1]

    if "!PB" in message.upper() and Config.CHANNEL.upper() == Config.USER.upper():
        send_message(open_socket, look_up_pb(Config.CATEGORY))

    if "!POINTS" == message.upper():
        send_message(open_socket, username + " has " + str(look_up_points(username)) + " " + point_name + ".")

    if "!QUOTE" in message.upper():
        parts = message.split()
        if 1 == len(parts):
            quote = get_quote('rand')
        else:
            quote = get_quote(parts[1])
        if not 'FAIL' == quote:
            send_message(open_socket, quote)

    if "!SLOTS" == message.upper():
        result = slots()
        send_message(open_socket,
                     "[ " + SlotEmotes.reverse_mapping[int(result[0])] + " ] [ " + SlotEmotes.reverse_mapping[int(result[1])] + " ] [ " + SlotEmotes.reverse_mapping[int(result[2])] + " ]")
        if result[0] == result[1] and result[1] == result[2]:
            send_message(open_socket, "Congratulations! Please cheer801 to redeem your reward!")

    if "!WR" == message.upper() and Config.CHANNEL.upper() == Config.USER.upper():
        send_message(open_socket, look_up_wr(Config.CATEGORY))

    if "!YORB" == message.upper():
        send_message(open_socket, "skip")
