import random


def load_quotes():
    f = open(r'/media/sf_D_DRIVE/Dev/EmoArbot/connor75.txt', 'rb')
    file_quotes = f.readlines()
    f.close()
    return file_quotes


def get_quote(num):
    if 'rand' == num:
        num = str(random.randrange(1, len(quotes)))
    if num.isdigit():
        num = int(num)
        if 0 <= num - 1 < len(quotes):
            return quotes[num - 1]
    return 'FAIL'


quotes = load_quotes()
