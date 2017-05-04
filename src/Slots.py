import random


def slots():
    slot1 = random.randrange(1, 11)
    slot2 = random.randrange(1, 11)
    slot3 = random.randrange(1, 11)

    return [slot1, slot2, slot3]
