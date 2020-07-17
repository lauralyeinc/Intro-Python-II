# Implement a class to hold room information. This should have name and
# description attributes.
from item import Item

"""
* Put the Room class in `room.py` based on what you see in `adv.py`.
√√ 
  * The room should have `name` and `description` attributes.   
    √√ 
!* The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    which point to the room in that respective direction.
    ?????
"""
class Room():
    def __init__(self, name, description, items = None):
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None  
        if items is None:
            self.items = []
        else:
            self.items = items

    def __str__(self):
        output = ""
        if self.n_to:
            output += "To the north is the " + self.n_to.name + '\n'
        if self.e_to:
            output += "To the east is the " + self.e_to.name + '\n'
        if self.s_to:
            output += "To the south is the " + self.s_to.name + '\n'
        if self.w_to:
            output += "To the west is the " + self.w_to.name + '\n'
            
        return output


    def __repr__(self):
        return f"self.name = {self.name} : self.description = {self.description}"

    def print_items(self):
        if len(self.items) > 0:
            print('This room as the following items to take: ')
            for i in self.items:
                print(f' {i.name} : {i.description}')
        else:
            print("There isn't any items in this room.")


    def search_items(self, item):
        for i in self.items:
            if i.name.lower() == item:
                return i 
        else: 
            print(f'That item is not in this room. Keep looking...')
            self.print_items()

    def add_item(self, item):
        self.items.append(item)

    def drop_item(self, item):
        self.items.remove(item)