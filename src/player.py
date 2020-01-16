# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        self.items = []

    def travel(self, direction):
        next_room = self.current_room.get_room_in_direction(direction)
        if next_room is not None:
            self.current_room = next_room
            print(f"Current room: {self.current_room}")
            print(', '.join(str(item.name)
                            for item in self.current_room.items))
        else:
            print("You cannot move in that direction")

    def print_inventory(self):
        if len(self.items) == 0:
            print("No items in your inventory")
            return
        print(', '.join(str(item.name)
                        for item in self.items))

    def add_item(self, room_item):
        for item in self.current_room.items:
            if item.name.lower() == room_item:
                self.items.append(item)
                self.current_room.remove_item(item)
                item.on_take()
                return
        print("No item with that name")

    def remove_item(self, current_item):
        for item in self.items:
            if item.name.lower() == current_item:
                self.current_room.add_item(item)
                self.items.remove(item)
                item.on_drop()
                return
        print("No item with that name in your inventory.")
