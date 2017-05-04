import string


def get_username(line):
    return string.split(string.split(line, ":")[1], "!")[0]


def get_message(line):
    message = string.split(line, ":")[2]
    return message[:len(message) - 1]
