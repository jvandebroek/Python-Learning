print "you enter a dark room with two doors. do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "there is a giant bear here eating cheese cake. what do you do?"
    print "1. take cake"
    print "2. scream at the bear"

    bear = raw_input("> ")

    if bear == "1":
        print "the bear eats your face off."
    elif bear == "2":
        print "the bear eats your legs off"
    else:
        print "well, doing %s is probably better. the bear runs away." % bear

elif door == "2":
    print "you stare into the endless abyss at cthulu's retina"
    print "1. blueberries"
    print "2. yellow jacket clothespin"
    print "3. understanding revolvers yelling melodies"

    insanity = raw_input("> ")

    if insanity == '1' or insanity == '2':
        print "your body survives powered my a mind of jello"
    else:
        print "the insanity rots your eyes into a pool of muck"

else:
    print "you stumble around and fall on a knife and die"

