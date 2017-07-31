import os
import random
import Config


def load_quotes():
    filename = os.path.join(os.path.dirname(__file__), "..", "resources", "quotes", Config.CHANNEL + ".txt")
    print filename
    try:
        f = open(filename, 'rb')
    except IOError:
        return 'FAIL'
    file_quotes = f.readlines()
    f.close()
    return file_quotes


def get_quote(num):
    quotes = load_quotes()
    if 'rand' == num:
        num = str(random.randrange(0, len(quotes)) + 1)
    if num.isdigit():
        num = int(num) - 1
        if 0 <= num < len(quotes):
            return quotes[num]
    return 'FAIL'


def add_quote(quote):
    filename = os.path.join(os.path.dirname(__file__), "..", "resources", "quotes", Config.CHANNEL + ".txt")
    try:
        f=open(filename, 'a+')
    except IOError:
        return
    msg = quote + "\n"
    f.write(msg)
