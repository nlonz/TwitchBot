import Config
from Categories import categories
from Enum import SlotEmotes
from Init import send_message
from Lookup import look_up_pb, look_up_wr
from Meme import meme
from Quote import get_quote
from Read import get_username, get_message
from Slots import slots


def executeCommand(open_socket, line):
    username = get_username(line)
    message = get_message(line)

    if "!ABOUT" == message.upper():
        send_message(open_socket,
                     "I am a bot designed by EmoArbiter for use in his Twitch channel. I am written in Python 2.7 and use the speedrun.com REST API for any leaderboard information. Any suggestions "
                     "for new features and feedback is welcome!")

    if "!DCW" in message.upper():
        send_message(open_socket, "For information on Delayed Cutscene Warp, read here: https://pastebin.com/3fQuCVB4")

    if "!EDITPASTEBIN" in message.upper() and "KONDITIONER" == username.upper() and "KONDITIONER" == Config.CHANNEL.upper():
        parts = message.split()
        if len(parts) >= 2:
            try:
                filename = "/media/sf_D_DRIVE/Dev/EmoArbot/resources/kondipastebin.txt"
                pastebin = open(filename, 'wb')
                pastebin.write(str(parts[1]))
                pastebin.close()
            except IOError:
                return
        else:
            send_message(open_socket, "Put a link here idiot")

    if "!FFM" in message.upper():
        send_message(open_socket, "For information on Furnace Fun Moves, read here: https://pastebin.com/rNaSUVqK")

    if "!MEME" in message.upper():
        send_message(open_socket, meme())

    if "!MMM" in message.upper():
        send_message(open_socket, "For information on Main Menu Mode, read here: https://pastebin.com/13hLcXww")

    if "!MODE" in message.upper() and Config.CHANNEL.upper() == username.upper() and Config.CHANNEL.upper() == Config.USER.upper():
        parts = message.split()
        category = parts[1]
        if category in categories:
            Config.CATEGORY = parts[1]

    if "!PASTEBIN" in message.upper() and "KONDITIONER" == username.upper() and "KONDITIONER" == Config.CHANNEL.upper():
        try:
            filename = "/media/sf_D_DRIVE/Dev/EmoArbot/resources/kondipastebin.txt"
            pastebin = open(filename, 'rb')
            link = pastebin.readlines()[0]
            pastebin.close()
        except IOError:
            return
        send_message(open_socket, link)

    if "!PB" in message.upper() and Config.CHANNEL.upper() == Config.USER.upper():
        send_message(open_socket, look_up_pb(Config.CATEGORY))

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
