class ShoppingCart:

    def __init__(self):
        self.items = []

    def add_item(self, name, quantity):
        item = (name, quantity)
        self.items.append(item)

    def remove_item(self, item_name):
        for item in self.items:
            if item[0] == item_name:
                self.items.remove(item)
                break
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1]
        return  total


