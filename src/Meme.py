import random


def meme():
    filename = "/media/sf_D_DRIVE/Dev/EmoArbot/resources/memes.txt"
    try:
        f = open(filename, 'rb')
    except IOError:
        return 'FAIL'
    memes = f.readlines()
    f.close()
    num = random.randrange(1, len(memes))
    return memes[num]
