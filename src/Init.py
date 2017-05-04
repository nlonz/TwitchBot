import socket
import string

from Config import HOST, PORT, PASS, NICK

CHANNEL = ""


def init(username):
    global CHANNEL
    CHANNEL = username
    s = socket.socket()
    s.connect((HOST, PORT))
    s.send("PASS " + PASS + "\r\n")
    s.send("NICK " + NICK + "\r\n")
    s.send("JOIN #" + CHANNEL + "\r\n")
    return s


def send_message(s, message):
    message = "PRIVMSG #" + CHANNEL + " :" + message + "\r\n"
    s.send(message)
    print("Sent: " + message)


def join_room(s):
    read_buffer = ""
    loading = True
    while loading:
        read_buffer = read_buffer + s.recv(1024)
        temp = string.split(read_buffer, "\n")
        read_buffer = temp.pop()

        for line in temp:
            print(line)
            loading = isLoadingComplete(line)
    print("Successfully joined chat")


def isLoadingComplete(line):
    if "End of /NAMES list" in line:
        return False
    else:
        return True
