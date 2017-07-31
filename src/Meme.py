import os
import random


def meme():
    filename = os.path.join(os.path.dirname(__file__), "..", "resources", "memes.txt")
    try:
        f = open(filename, 'rb')
    except IOError:
        return 'FAIL'
    memes = f.readlines()
    f.close()
    num = random.randrange(1, len(memes))
    return memes[num]
