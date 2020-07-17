from room import Room     # need to set up a class called room! 
from player import Player # built out a class called new_player stored, current_room & items 

'''
* Add a REPL parser to `adv.py` that accepts directional commands to move the new_player
  * After each move, the REPL should print the name and description of the new_player's current room
  * Valid commands are `n`, `s`, `e` and `w` which move the new_player North, South, East or West
  * The parser should print an error if the new_player tries to move where there is no room.
'''

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                    "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

#
# Main
#

# Make a new new_player object that is currently in the 'outside' room. 
# player = Player('Laura', room['outside'])
# user can input their own unqiue name. 
playerName = input('Please enter a name for your hero: ')
hero = Player(playerName, room['outside'])


from item import Item 

# create an item 
sword = Item("sword", "Sword made of gold")
# add item to the room
room['foyer'].add_item(sword)

map = Item('map', "The secrets to the land")
room['outside'].add_item(map)

latern = Item('latern', 'Help you see the way')
room['overlook'].add_item(latern)

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# start prompt
print(f'\n Hello, {hero.name} \n Current Room: {hero.current_room.name}\n')
print(room['outside'].description)
print('''\n Here's a map to help you find your way to the treasure or live. Type 'get map' or 'take map' to add it to your inventory.\n To remove an item, type 'drop map'. Try it out!\n ''')

# direction & action conditions 
directions = ['n', 'e', 's', 'w']
item_actions = ['get', 'take', 'drop']

#while loop
while True:
    #player selection to play, inputs 
    player_input = input("\n Let's go! Onward! \n n for north, s for south, e for east, w for west, \nget [ITEM], take [ITEM], drop [ITEM], i for inventory, or q to quit the game: \n").lower().split(' ')

    # player selections/input wrong. error handling 
    if len(player_input) > 2 or len(player_input) < 1:
        print("Invalid entry. Please try again.")

    #action of player get take or drop an item.  condiontal for actions
    elif len(player_input) == 2:
        if player_input[0] in item_actions:
            if player_input[0] == 'get' or player_input[0] == 'take':
                item = hero.current_room.search_items(player_input[1])
                if item in hero.current_room.items:
                    hero.current_room.drop_item(item)
                    hero.add_item(item)
                    item.on_take(item)
                else:
                    print('\n This item does not exist. Try again...')

            elif player_input[0] == 'drop':
                item = hero.search_items(player_input[1])
                if item in hero.inventory:
                    hero.current_room.add_item(item)
                    hero.drop_item(item)
                    item.on_drop(item)
                else:
                    print('\n There are no items in your inventory.')
    else: 
    # direction actions
        if player_input[0] in directions:
            try: 
                hero.move_room(player_input[0])
                print(f'\n You are in the {hero.current_room.name}: \n {hero.current_room.description} \n')
                print(hero.current_room)
                hero.current_room.print_items()
            except AttributeError:
                    print("\n There isn't a room in that direction, Keep searching.....")

            #inventory 
        elif player_input[0] == 'i' or player_input[0] == 'inventory':
                if hero.inventory:
                    print(f'\n{hero.name}, these are the items you have:')
                    for items in hero.inventory:
                        print(f'{items}')
                else:
                    print('\n It seems to be, there is not a thing in your inventory.')

        # quit the game
        elif player_input[0] == 'q':
            print('\n Until next time!')
            exit()
        
        #error handiling for the directions
        else: 
            print("\n Can't go that way, try again. ")



