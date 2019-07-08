from sys import exit
from random import randint
import ex43_rooms  #Obviously this entire game could be just one file, but if it were to get more complicated with an inventory and the like it might be worth using different files for different things. In this case I just have one for the "map" and one for running the game.

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
        
aMap = ex43_rooms.Map('WakeUp')
aGame = Engine(aMap)
aGame.play()







        
