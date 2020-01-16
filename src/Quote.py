import random
import Config


def load_quotes():
    print Config.CHANNEL
    filename = "somepath" + Config.CHANNEL + ".txt"
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
        num = str(random.randrange(1, len(quotes)))
    if num.isdigit():
        num = int(num)
        if 0 <= num - 1 < len(quotes):
            return quotes[num - 1]
    return 'FAIL'
