# Write a class to hold player information, e.g. what room they are in
# currently.


class Player():
    def __init__(self, room, items):
        self.room = room
        self.items = items
        self.item_names = [item.name for item in self.items]

    def add_item(self, item):
        self.items.append(item)
        item.on_take()

    def remove_item(self, item):
        self.items.remove(item)
        itm.on_drop()
