from sys import exit

def gold_room():
    print "this room is full of gold, how much do you take?"
    next = raw_input("> ")
    if next.isdigit():
        how_much = int(next)
    else:
        dead("man learn to type a number.")

    if how_much < 50:
        print "nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("you greedy bastard!")
def bear_room():
    print "there is a bear here"
    print "the bear has a bunch of honey"
    print "the fat bear is in from of another door"
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("the bear looks at you then pimp slaps your face off")
        elif next == "taunt bear" and not bear_moved:
            print "the bear has moved from the door. you can go through now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("the bear gets pissed and chews your crotch off")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means"

def cthulu_room():
    print "here you see the great evil cthulu"
    print "he, it, whatever stares at you and you go insane"
    print "do you flee for your life or eat your head?"
    next = raw_input("> ")
    if "flee" in next:
        start()
    elif "head" in next:
        dead("well that was tasty")
    else:
        cthulu_room()

def dead(why):
    print why, "good job!"
    exit(0)

def start():
    print " You are in a dark room\n there is a door to your right and left\n which one do you take?"
    next = raw_input("> ")
    if next == "left":
        bear_room()
    if next == "right":
        cthulu_room()
    else:
        dead("you stumble around the room until you starve")

start()
    
