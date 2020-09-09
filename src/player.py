# Write a class to hold player information, e.g. what room they are in
# currently.
'''
* Put the Player class in `player.py`.
√√ 
  * Players should have a `name` and `current_room` attributes
√√ 
'''

class Player:  # <-- class set up 
    def __init__(self, name, current_room):  # <-- init a player with name, location, and a way to hold items. 
        self.name = name
        self.current_room = current_room


    def __str__(self):  # set up function to return the players name to use outside of player.py 
        return f'{self.name} is currently in Room: {self.current_room}'

    def __repr__(self):
        return f'self.name= {self.name} : self.current_room = {self.current_room}'
    
    def move_room(self, direction):
        if getattr(self.current_room, f'{direction}_to'):
            self.current_room = getattr(self.current_room, f'{direction}_to')
        else:
            print('\n There is nothing in that direction, try a different direction. \n')