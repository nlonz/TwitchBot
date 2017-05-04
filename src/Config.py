# Config.py

# User is defined as the person who runs the bot

HOST = "irc.chat.twitch.tv"
PORT = 6667
CHANNEL = ""
# USER = User's Twitch username
# CATEGORY = "Category you are running. Only useful in the user's channel"
# NICK = Bot's Twitch username
# PASS = The bot's IRC password for Twitch chat
# SRCUSER = User's speedrun.com username
# LOYALTYPATH = Path to loyalty database. Only useful in the user's channel
# CLIENTID = Twitch API Key


def configure():
    global CHANNEL
    CHANNEL = ""
