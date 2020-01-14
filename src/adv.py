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
player = Player(room['outside'], [])


def list_to_string(items):
    new_str = ""

    for item in items:
        new_str += item + " "
    return new_str


end = False
while end != True:
    print(player.room.name)
    wrapper = textwrap.TextWrapper(width=70)

    description = wrapper.wrap(
        text=player.room.description + "\n")

    print("Items in room: ")

    item_names = []
    for item in player.room.items:
        item_names.append(item.name)
        print(f"{item.name}")

    for word in description:
        print(word)
    user_input = input("Choose a room: ")

    first_word = user_input.split()[0]

    if user_input == "n":
        if hasattr(player.room, "n_to"):
            player.room = player.room.n_to
        else:
            print("You are not allowed to move in that direction")
    if user_input == "s":
        if hasattr(player.room, "s_to"):
            player.room = player.room.s_to
        else:
            print("You are not allowed to move in that direction")
    if user_input == "e":
        if hasattr(player.room, "e_to"):
            player.room = player.room.e_to
        else:
            print("You are not allowed to move in that direction")
    if user_input == "w":
        if hasattr(player.room, "w_to"):
            player.room = player.room.w_to
        else:
            print("You are not allowed to move in that direction")
    if first_word == "drop":
        second_word = user_input.split()[1]
        if not player.items:
            print("You don't have any items to drop off")
        else:
            if second_word in player.items:
                item_index = item_names.index(second_word)
                player.remove_item(player.room.items[item_index])
                player.room.items.remove(player.room.items[item_index])
                print(item_to_drop + " has been dropped in " +
                      player.room.name)
        # logic for dropping item
    elif first_word == "get" or first_word == "take":
        second_word = user_input.split()[1]
        if (second_word in item_names):
            item_index = item_names.index(second_word)
            player.add_item(player.room.items[item_index])
            player.room.items.remove(player.room.items[item_index])
            print(second_word + " has been added from " +
                  player.room.name)
    if first_word == "i":
        print(list_to_string(player.item_names))

        # logic for adding item
    if first_word == "q":
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
