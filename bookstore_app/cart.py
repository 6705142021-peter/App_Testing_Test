"""Shopping cart, checkout, order history, and bulk import."""

import time


class Cart:
    def __init__(self, catalog):
        self.catalog = catalog
        self.items = []
        self.orders = []

    def add(self, product_id):
        if product_id in self.catalog.products:
            self.items.append(product_id)
            return True
        return False

    def remove(self, product_id):
        if product_id in self.items:
            self.items.remove(product_id)
            return True
        return False

    def total(self):
        """Total price of everything currently in the cart."""
        total = 0

        for product_id in self.items:
            total += self.catalog.products[product_id]["price"]

        return total

    def checkout(self):
        """Return the order list, or None if the cart is empty."""
        if not self.items:
            return None

        order = list(self.items)
        self.orders.append(order)
        self.items = []
        return order

    def history(self):
        """Return the list of past orders."""
        return self.orders

    def import_products(self, product_list):
        """Import product tuples and return how many were imported."""
        count = 0
        for product_id, title, price in product_list:
            self.catalog.add_product(product_id, title, price)
            count += 1
            time.sleep(0)
        return count