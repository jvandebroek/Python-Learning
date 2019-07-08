from sys import exit
from random import randint
import inventory
import lexicon
import sentence

class WakeUp(object):
    def enter(self):
        print """Welcome to my game, please type in "full" sentences at all times I.E. "Enter the Room" when giving commands\n------------------------\n
        You awake in a spaceship on what appears to be an operating table
look down and see you are wearing what looks like a hospital gown. 
Suddenly you hear the sound of someone approaching from the main door way.
You frantically look around and see that there is another doorway and a closet.
You also see a scalpel on the table, you are running out of time, what do you do?"""
        action = raw_input("> ")
        if sentence.parse_sentence(lexicon.scan(action)).object == 'closet':
            print """You hide in the closet and see as an alien enters the room,
The alien looks paniced that you are not on the operating table and presses
a large emergency button on the wall before leaving the room.
red lights start flashing and a gas enters the room,
You breath in the gas and pass out."""
            return 'WakeUp'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'doorway' or sentence.parse_sentence(lexicon.scan(action)).object == 'door':
            print """you run out the back door"""
            return 'Hallway'
        elif sentence.parse_sentence(lexicon.scan(action)).verb == 'leave' or sentence.parse_sentence(lexicon.scan(action)).verb == 'exit':
            print """you run out the back door"""
            return 'Hallway'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'scalpel':
            print """An alien enters the room and sees you holding a scalpel
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
what do you do?"""
        action = raw_input("> ")
        if sentence.parse_sentence(lexicon.scan(action)).object == 'Escape':
            print """The door is locked but there is a keypad"""
            return 'EscapePod'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'Office':
            print """You open the door and slip inside without being detected"""
            return 'Office'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'Weaponry' or sentence.parse_sentence(lexicon.scan(action)).object == 'weaponry':
            print """You open the door and slip in undetected."""
            return 'Weaponry'
        else:
            print "The alien hears you fumbling around and shoots, you die"
            return 'death'
class Weaponry(object):
    def enter(self):
        print """You see a large selection of guns. You decide it would be prudent to take one before continuing on your adventure. There is a pistol, a machine gun and a grenade."""
        action = raw_input("> ")
        if sentence.parse_sentence(lexicon.scan(action)).object == 'pistol':
            print """You grab the pistol and head back into the Hallway"""
            inventory.items.pickup('pistol')
            return 'Hallway2'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'machine':
            print """You pick up the machine gun, but this actions triggers and alarm, alien guards come rushing in and kill you before you can even figure out how to shoot the thing."""
            return 'death'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'grenade':
            print """You grab the grenade and head back into the Hallway"""
            inventory.items.pickup('grenade')
            return 'Hallway2'
        else:
            print "The alien hears you fumbling around and shoots, you die"
            return 'death'
class Hallway2(object):
    def enter(self):
        if inventory.items.holding('key'):
            print "all thats left is to escape via the escape pod! You head to that door and find it locked by a keypad."
            return 'EscapePod'
        else:
            print "As you re-enter the hallway the alien spots you and attacks! You have no choice but to try to defend yourself."
            if inventory.items.holding('pistol'):
                print """You quickly draw your pistol and shoot the alien, after searching his body you find what looks like a car key. Where do you want to go now? The escape pod or the office?"""
                inventory.items.pickup('key')
                action = raw_input("> ")
                if sentence.parse_sentence(lexicon.scan(action)).object == 'Escape' or sentence.parse_sentence(lexicon.scan(action)).object == 'escape':
                    print "You head to the door labeled 'escape pod' and find it locked with a keypad..."
                    return 'EscapePod'
                elif sentence.parse_sentence(lexicon.scan(action)).object == 'Office' or sentence.parse_sentence(lexicon.scan(action)).object == 'office':
                    print "You decide to snoop around a bit more before leaving and enter the office."
                    return 'Office'
                else:
                    print "The ceiling collapses and you die!"
                    return 'death'
                    
            elif inventory.items.holding('grenade'):
                print """You throw the grenade at the alien in a panic, the explosion blows open the walls of the ship sucking you into space"""
                return 'death'
            else:
                print "The alien has no problem dealing with an unarmed human such as yourself"
                return 'death'
class EscapePod(object):
    def enter(self):
        print """You look down at the keypad and realize you dont have time to go to another door, you realize you have to guess What code do you enter?"""
        action = raw_input("> ")
        if sentence.parse_sentence(lexicon.scan(action)).object == 8956:
            print """The door opens and you find yourself in the cockpit of an escape pod"""
            if inventory.items.holding('key'):
                print """You launch the ship into space and set the course for earth, you are free!"""
                return 'Win'
            else:
                print """You dont have a key the launch the space craft! The alien guards captures you before you can make another move"""
            return 'death'

        else:
            print "The keypad loudly beeps to inform you that the code was incorrect, this alerts nearby aliens who shoots you dead."
            return 'death'
class Office(object):
    def enter(self):
        print """It looks just like a human office. You see a computer a file cabinet and a closet what do you do? (you can also always leave)"""
        action = raw_input("> ")
        if sentence.parse_sentence(lexicon.scan(action)).object == 'computer':
            print """The computer is locked and the attempt to login causes an alarm to go off, aliens flood in to the room and detain you knocking you out."""
            return 'WakeUp'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'closet':
            print """You open the closet and are terrified to find that it is full of human skins on coat hangers as though they are clothes, They look alarmingly like many of the politicians you sometimes see on TV. you look around the office again."""
            return 'Office'
        elif sentence.parse_sentence(lexicon.scan(action)).object == 'file' or sentence.parse_sentence(lexicon.scan(action)).object == 'cabinet':
            print """You open filecabinet and start looking through the files, its all written in nonsense alien languages The only thing you can make out are the numbers 8956, you look around the office again"""
            return 'Office'
        elif sentence.parse_sentence(lexicon.scan(action)).verb == 'leave' or sentence.parse_sentence(lexicon.scan(action)).verb == 'exit':
            print "Satified with your investigation you head back into the hallway"
            return 'Hallway2'
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
        'Weaponry': Weaponry(),
        'Hallway2':Hallway2()
    }

    def __init__(self, start):
        self.start = start

    def next(self, name):
        where = Map.rooms.get(name)
        return where

    def opening_scene(self):
        return self.next(self.start)














