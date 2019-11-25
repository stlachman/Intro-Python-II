import textwrap
from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ["candlestick", "cigar", "match"]),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ["candlestick", "cigar", "match"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ["candlestick", "cigar", "match"]),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", ["candlestick", "cigar", "match"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ["candlestick", "cigar", "match"]),
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
player = Player(room['outside'], [])


def list_to_string(items):
    new_str = ""

    for item in items:
        new_str += item + " "
    return new_str


end = False
while end != True:
    print(player.room.name)
    wrapper = textwrap.TextWrapper(width=50)

    description = wrapper.wrap(
        text=player.room.description + "\n               " + "Items in room: " + list_to_string(player.room.items))

    for word in description:
        print(word)
    user_input = input("Choose a room: ")
    if user_input == "n":
        if hasattr(player.room, "n_to"):
            player.room = player.room.n_to
        else:
            print("Not allowed to move there")
    if user_input == "s":
        if hasattr(player.room, "s_to"):
            player.room = player.room.s_to
        else:
            print("Not allowed to move there")
    if user_input == "e":
        if hasattr(player.room, "e_to"):
            player.room = player.room.e_to
        else:
            print("Not allowed to move there")
    if user_input == "w":
        if hasattr(player.room, "w_to"):
            player.room = player.room.w_to
        else:
            print("Not allowed to move there")
    if user_input == "i":
        print(list_to_string(player.room.items))
        item_user_input = input(
            "\nWould you like to pick up an item from this room? Or drop off an item in this room?\n")

        if item_user_input == "d":
            if not player.items:
                print("You don't have any items to drop off")
            else:
                item_to_drop = input("Which item would you like to drop off?")
                if item_to_drop in player.items:
                    player.room.items.append(item_to_drop)
                    player.items.remove(item_to_drop)
                    print(item_to_drop + " has been dropped in " +
                          player.room.name)
            # logic for dropping item
        elif item_user_input == "a":
            item_to_add = input("Which item would you like to add?")
            if (item_to_add in player.room.items):
                player.items.append(item_to_add)
                player.room.items.remove(item_to_add)
                print(item_to_add + " has been added from" +
                      player.room.name)
            # logic for adding item
    if user_input == "q":
        end = True

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
