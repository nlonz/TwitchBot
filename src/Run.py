import json
import string
import time
import urllib2
from multiprocessing import Process

from Commands import executeCommand
from Config import CLIENTID
from Init import init, join_room


def run(username):
    open_socket = init(username)
    join_room(open_socket)
    read_buffer = ""

    while True:
        read_buffer = read_buffer + open_socket.recv(1024)
        temp = string.split(read_buffer, "\n")
        read_buffer = temp.pop()

        for line in temp:
            if "PING" in line:
                open_socket.send("PONG\r\n")
                break

            else:
                executeCommand(open_socket, line)
        time.sleep(0.1)


# def is_online(username):
#     stream = get_stream_info(username)

#     while stream is None:
#         time.sleep(60)
#         stream = get_stream_info(username)

#     print username + " is online"


# def is_offline(username):
#     stream = get_stream_info(username)

#     while stream is not None:
#         time.sleep(60)
#         stream = get_stream_info(username)

#     print username + " is offline"


# def parent_process(username):
#     p_run = Process(target=run, args=(username,))
#     p_online = Process(target=is_online, args=(username,))
#     p_offline = Process(target=is_offline, args=(username,))

#     while True:
#         print "Starting online for " + username
#         p_online.start()
#         p_online.join()
#         print "Starting run for " + username
#         p_run.start()
#         print "Starting is_offline for " + username
#         p_offline.start()
#         p_offline.join()
#         print "Terminating run for " + username
#         p_run.terminate()
#         p_run = Process(target=run, args=(username,))
#         p_online = Process(target=is_online, args=(username,))
#         p_offline = Process(target=is_offline, args=(username,))
#         time.sleep(0.5)


# def get_stream_info(username):
#     url = "https://api.twitch.tv/kraken/streams/" + username + "?client_id=" + CLIENTID
#     return json.loads(urllib2.urlopen(url).read().decode("utf-8")).get("stream")


# if __name__ == '__main__':
#     p1 = Process(target=parent_process, args=("gajbp",))
#     p1.start()
#     # p2 = Process(target=parent_process, args=("konditioner",))
#     # p2.start()
run("gajbp")