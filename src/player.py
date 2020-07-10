# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:  # <-- class set up 
    def __init__(self, name, location):  # <-- init a player with name, location, and a way to hold items. 
        self.name = name
        self.location = location
        self. items = []

    def get_item(self, item):  #  set up a way to get items to add them, and remove them. Also add a way to tell the user what they picked up. 
        self.location.remove_item(item)
        self.items.append(item)
        return f'You picked up {item.name}'

    def __str__(self):  # set up function to return the players name to use outside of player.py 
        return f'{self.name}'