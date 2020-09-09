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
player = Player('Laura', room['outside'])
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
print(f'\n Hello, {player.name} \n Current Room: {player.current_room.name}\n')
print(room['outside'].description)

# direction conditions 
directions = ['n', 'e', 's', 'w']

#while loop
while True:
    #player selection to play, inputs 
    player_input = input("\n Let's go! Onward! \n n for north, s for south, e for east, w for west, q to quit the game: \n")
    # player selections/input wrong. error handling 
    if len(player_input) > 2 or len(player_input) < 1:
        print("Invalid entry. Please try again.")
    
    else: 
    # direction actions
        if player_input[0] in directions:
            try: 
                player.move_room(player_input[0])
                print(f'\n You are in the {player.current_room.name}: \n {player.current_room.description} \n')
                # print(player.current_room)
            except AttributeError:
                    print("\n There isn't a room in that direction, Keep searching.....")

        # quit the game
        elif player_input[0] == 'q':
            print('\n Until next time!')
            exit()
        
        #error handiling for the directions
        else: 
            print("\n Can't go that way, try again. ")



