from sys import exit
from random import randint
import rooms  
import inventory

class Engine(object):

    def __init__(self, room_map):
        self.room_map = room_map

    def play(self):
        current_room = self.room_map.opening_scene()
        last_room = self.room_map.next('Win')

        while current_room != last_room:
            print "\n ------------------------"
            next_room = current_room.enter()
            current_room = self.room_map.next(next_room)

        current_room.enter()
        
aMap = rooms.Map('WakeUp')
aGame = Engine(aMap)
aGame.play()







        
