import textwrap
from room import Room
from player import Player
from item import Item
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", [Item("candlestick", "it helps you find your way in the dark"), Item("cigar", "smoking is fun"), Item("match", "used for smoking")]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", [Item("coin", "Gold and shiny"), Item("sword", "used in war"), Item("wine", "red and white")]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", [Item("goblet", "for wine"), Item("knife", "sneaky"), Item("shield", "defense")]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", [Item("poison", "sneakier"), Item("lamp", "lamp lamps"), Item("pipe", "More tobacco")]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", [Item("pie", "cherry pie"), Item("wood", "burning wood"), Item("saw", "used for wood")]),
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


# Make a new player object that is currently in the 'outside' room.

player = Player(input("Please enter your name: "), room["outside"])

directions = ["n", "s", "e", "w"]

while True:
    cmd = input("-----> ").lower()

    if cmd.split()[0] == "get" or cmd.split()[0] == "take":
        player.add_item(cmd.split()[1])
    elif cmd.split()[0] == "drop":
        player.remove_item(cmd.split()[1])
    elif cmd in directions:
        player.travel(cmd)
    elif cmd == 'i' or cmd == "inventory":
        player.print_inventory()
    elif cmd == "q":
        print("Goodbye")
        break
    else:
        print("I did not recognize that command")

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
