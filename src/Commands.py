#!/usr/bin/python
# -*- coding: iso-8859-15 -*-
import Config
from Categories import categories
from Enum import SlotEmotes, SlutEmotes
# from Gamble import gamble, look_up_points, point_name
from Init import send_message
from Lookup import look_up_pb, look_up_wr
from Quote import get_quote
from Read import get_username, get_message
from Slots import slots


def executeCommand(open_socket, line):
    username = get_username(line)
    message = get_message(line)

    if "!ABOUT" == message.upper():
        send_message(open_socket,
                    "I am a bot designed by EmoArbiter for use in his Twitch channel. I am written in Python 2.7 and use the speedrun.com REST API for any leaderboard information. Any "
                    "suggestions for new features and feedback is welcome!")

    if "!ALPHA" == message.upper():
        send_message(open_socket, "https://youtu.be/y0-X9O4nmzY")

    if "!BANJO" == message.upper():
        send_message(open_socket, "DONT 👏 CALL 👏 YOURSELF 👏 A 👏 BANJO 👏 RUNNER 👏 IF 👏 YOU 👏 DONT 👏 LOVE 👏 SUCKING 👏 DICK 👏")

    if "!BATISTA" == message.upper():
        send_message(open_socket, "https://clips.twitch.tv/HomelyPhilanthropicMoonStoneLightning")

    if "!BT" == message.upper():
        send_message(open_socket, "💯 100 💯 ⏰ Clockworks ⏰ ⬇ Down ⬇ the 🚽 Toilet 🚽")

    if "!COMMANDS" == message.upper():
        send_message(open_socket, "Available commands are !301, !about, !commands, !pb, !points, !wr")

    if "!DCW" == message.upper():
        send_message(open_socket, "For information on Delayed Cutscene Warp, read here: https://pastebin.com/3fQuCVB4")

    if "!FFM" == message.upper():
        send_message(open_socket, "For information on Furnace Fun Moves, read here: https://pastebin.com/rNaSUVqK")

    # if "!GAMBLE" in message.upper():
    #     send_message(open_socket, gamble(username, message))

    if "!GGMEARLY" == message.upper():
        send_message(open_socket, "https://clips.twitch.tv/TenaciousBillowingCamelSwiftRage")

    if "!GMG" == message.upper():
        send_message(open_socket, "https://clips.twitch.tv/VenomousFragileTapirPJSalt")

    if "!KONDITIOENR" == message.upper():
        send_message(open_socket, 
                    "In my opinion, Konditioenr is a sellout piece of shit. I am over here practicing and really trying to improve my speed game, and he is over there DICK riding other top "
                    "streamers just to get a sub button. It makes me sick. He is the kind of scum that ruins the speedrunning community. All he cares about is how much money he makes "
                    "instead of the quality of his speedruns. What a fucking joke.")

    if "!KONDITIONER" == message.upper():
        send_message(open_socket, "https://www.twitch.tv/videos/43226642")

    # if "!MODE" in message.upper() and Config.CHANNEL.upper() == username.upper() and Config.CHANNEL.upper() == Config.USER.upper():
    #     parts = message.split()
    #     category = parts[1]
    #     if category in categories:
    #         Config.CATEGORY = parts[1]

    if "!PB" in message.upper():# and Config.CHANNEL.upper() == Config.USER.upper():
        send_message(open_socket, look_up_pb(Config.CATEGORY))

    # if "!POINTS" == message.upper():
    #     send_message(open_socket, username + " has " + str(look_up_points(username)) + " " + point_name + ".")

    # if "!QUOTE" in message.upper():
    #     parts = message.split()
    #     if 1 == len(parts):
    #         quote = get_quote('rand')
    #     else:
    #         quote = get_quote(parts[1])
    #     if not 'FAIL' == quote:
    #         send_message(open_socket, quote)

    if "!SLOTS" == message.upper():
        result = slots(1, 14)
        send_message(open_socket,
                     "[ " + SlotEmotes.reverse_mapping[int(result[0])] + " ] [ " + SlotEmotes.reverse_mapping[int(result[1])] + " ] [ " + SlotEmotes.reverse_mapping[int(result[2])] + " ]")
        if result[0] == result[1] and result[1] == result[2]:
            send_message(open_socket, "Congratulations! Please cheer801 to redeem your reward!")

    if "!SLUTS" == message.upper():
        result = slots(1, 7)
        send_message(open_socket,
                     "[ " + SlutEmotes.reverse_mapping[int(result[0])] + " ] [ " + SlutEmotes.reverse_mapping[int(result[1])] + " ] [ " + SlutEmotes.reverse_mapping[int(result[2])] + " ]")
        if result[0] == result[1] and result[1] == result[2]:
            send_message(open_socket, "Congratulations! Please cheer801 to redeem your reward!")

    if "!TGUMP" == message.upper():
        send_message(open_socket, 
                    "TGUMP YOU ARE THE BIGGEST MOTHER FUCKING IDIOTIC BASTARD TWAT WAFFLE THAT I HAVE EVER MET, YOU ARE DUMBER THAN ME AND THATS SAYING SOMETHING. ITS PROBABLY A WORLD "
                    "RECORD TO BE HONEST")

    if "!TWITTER" == message.upper():
        send_message(open_socket, "http://twitter.com/emoarbiter")

    if "!VC" == message.upper():
        send_message(open_socket, 
                    "Yet somehow Virtual Console emulation is more acceptable than other forms of emulation. And the only reason I can surmise that this is the case is because the Virtual "
                    "Console is an officially licensed product from a huge corporation as opposed to a fan-made creation. Why are some emulators acceptable for speed running but others "
                    "aren't?")

    if "!WAIFU" == message.upper():
        send_message(open_socket, "https://www.twitch.tv/videos/41776563")

    if "!WILLTHISPB" == message.upper():
        send_message(open_socket, "No.")

    if "!WORLDRECORD" == message.upper():
        send_message(open_socket, "Can you PLEASE not use the term \"world record'? Instead please use the term BKTWVEAAAVBMOFSRC (best known time with video evidence as approved and "
            "verified by members of the speed running community) in the future. This would help lower confusion in these types of videos in regard to the ever updating and evolving "
            "nature of the speedrunning community.")

    if "!WR" == message.upper() or "!BKTWVEAAAVBMOFSRC" == message.upper():# and Config.CHANNEL.upper() == Config.USER.upper():
        send_message(open_socket, look_up_wr(Config.CATEGORY))

    if "!YORB" == message.upper():
        send_message(open_socket, "skip")
