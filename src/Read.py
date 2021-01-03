import string


def get_username(line):
    return line.split(":")[1].split("!")[0]
    #return string.split(string.split(line, ":")[1], "!")[0]


def get_message(line):
    message = line.split(":", 2)[2]
    #message = string.split(line, ":", 2)[2]
    return message[:len(message) - 1]
