from sys import exit
from random import randint

class WakeUp(object):
    def enter(self):
        print """You awake in a spaceship on what appears to be an operating table
look down and see you are wearing what looks like a hospital gown. 
Suddenly you hear the sound of someone approaching from the main door way.
You frantically look around and see that there is a back door and a closet.
You also see a scalpel on the table, you are running out of time, what do you do?
'enter closet', 'leave through the back', or 'grab scalpel'"""
        action = raw_input("> ")
        if action == 'enter closet':
            print """You hide in the closet and see as an alien enters the room,
The alien looks paniced that you are not on the operating table and presses
a large emergency button on the wall before leaving the room.
red lights start flashing and a gas enters the room,
You breath in the gas and pass out."""
            return 'WakeUp'
        elif action == 'leave through the back':
            print """you run out the back door"""
            return 'Hallway'
        elif action == 'grab scalpel':
            print """an alien enters the room and sees you holding a scalpel
                  he quickly grabs his laser gun off his belt and shoots you"""
            return 'death'
        else:
            print "Your eyes are tired and you fall asleep"
            return 'WakeUp'

class Hallway(object):
    def enter(self):
        print """You find yourself in a long hallway with an alien at the end of the hall
luckily he is looking the other way. There are three doors that you think you can 
sneak to without being detected. One is labeled 'Escape Pod', one is 'Office' and the final is 'Weaponry'
which do you enter?"""
        action = raw_input("> ")
        if action == 'Escape Pod':
            print """The door is locked but there is a keypad"""
            return 'EscapePod'
        elif action == 'Office':
            print """You open the door and slip inside without being detected"""
            return 'Office'
        elif action == 'Weaponry':
            print """You open the door and slip in undetected. unfortunately the room is full of heavily armed aliens, they are quick to kill you"""
            return 'death'
        else:
            print "The alien hears you fumbling around and shoots, you die"
            return 'death'
class EscapePod(object):
    def enter(self):
        print """You look down at the keypad and realize you dont have time to go to another door, you realize you have to guess What code do you enter?"""
        action = raw_input("> ")
        if action == '8956':
            print """The door opens and you find yourself in the cockpit of an escape pod, You launch the ship into space and set the course for earth, you are free!"""
            return 'Win'

        else:
            print "The keypad loudly beeps to inform you that the code was incorrect, this alerts the nearby alien who shoots you dead."
            return 'death'
class Office(object):
    def enter(self):
        print """It looks just like a human office. You see a 'computer' a 'file cabinet' and a 'closet' what do you look at? (you can also 'leave')"""
        action = raw_input("> ")
        if action == 'computer':
            print """The computer is locked and the attempt to login causes an alarm to go off, aliens flood in to the room and detain you knocking you out."""
            return 'WakeUp'
        elif action == 'closet':
            print """You open the closet and are terrified to find that it is full of human skins on coat hangers as though they are clothes
                  They look alarmingly like many of the politicians you sometimes see on TV"""
            return 'Office'
        elif action == 'file cabinet':
            print """You open filecabinet and start looking through the files, its all written in nonsense alien languages
                  The only thing you can make out are the numbers 8956"""
            return 'Office'
        elif action == 'leave':
            print "Satified with your investigation you head back into the hallway"
            return 'Hallway'
        else:
            print "The door to the office opens and an alien enters, he is quick to shoot you on sight, you die"
            return 'death'
            
class death(object):

    quips = [
        "You died.  You kinda suck at this.",
         "Your mom would be proud...if she were smarter.",
         "Such a luser.",
         "I have a small puppy that's better at this."
    ]

    def enter(self):
        print death.quips[randint(0, len(self.quips)-1)]
        exit(1)

class Win(object):

    def enter(self):
        print "You won! Good job."
        return 'finished'


class Map(object):

    rooms = {
        'Hallway': Hallway(),
        'Office': Office(),
        'EscapePod': EscapePod(),
        'WakeUp': WakeUp(),
        'Win': Win(),
        'death': death(),
    }

    def __init__(self, start):
        self.start = start

    def next(self, name):
        where = Map.rooms.get(name)
        return where

    def opening_scene(self):
        return self.next(self.start)














