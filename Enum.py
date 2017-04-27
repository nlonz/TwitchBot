def enum(**enums):
	return type('Enum', (), enums)
	
def enum(*sequential, **named):
    enums = dict(zip(sequential, range(len(sequential))), **named)
    reverse = dict((value, key) for key, value in enums.iteritems())
    enums['reverse_mapping'] = reverse
    return type('Enum', (), enums)
	
Month = enum(January = 1, February = 2, March = 3, April = 4, May = 5, June = 6,
	July = 7, August = 8, September = 9, October = 10, November = 11, December = 12)
	
SlotEmotes = enum(FrankerZ = 1, Jebaited = 2, CoolCat = 3, TriHard = 4, BabyRage = 5, TehePelo = 6,
	OpieOP = 7, OhMyDog = 8, EleGiggle = 9, PJSalt = 10, CoolStoryBob = 11, VoHiYo = 12, NotLikeThis = 13)