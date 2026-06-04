# shopping_cart.py
"""
Docstring for exercises.shopping_cart
"""


class ShoppingCart:
    """A simple shopping cart class to manage items and calculate totals"""

    def __init__(self):
        self.items = []

    def add_item(self, item, price):
        """Add an item with its price to the shopping cart"""
        self.items.append({"item": item, "price": price})

    def get_total(self):
        """Calculate and return the total price of all items in the cart"""
        return sum(item["price"] for item in self.items)

    def item_count(self):
        """Return the total number of items in the cart"""
        return len(self.items)

    def remove_item(self, item):
        """Remove an item from the shopping cart"""
        self.items.remove(item)

    def clear(self):
        """Remove all items from the shopping cart"""
        self.items.clear()

    def apply_discount(self, percent):
        """Apply a discount percentage (0-100) to the total"""
        if 0 <= percent <= 100:
            total = self.get_total()
            discount = total * (percent / 100)
            return total - discount
        raise ValueError("Discount percent must be between 0 and 100")