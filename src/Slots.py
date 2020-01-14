import random


def slots(min, max):
    slot1 = random.randrange(min, max)
    slot2 = random.randrange(min, max)
    slot3 = random.randrange(min, max)

    return [slot1, slot2, slot3]
