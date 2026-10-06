"""Product catalog: adding products and searching."""


class Catalog:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, title, price):
        self.products[product_id] = {
            "title": title,
            "price": price,
        }

    def search(self, keyword):
        """Return product IDs whose title contains the keyword."""
        results = []

        for product_id, info in self.products.items():
            if keyword in info["title"]:
                results.append(product_id)

        return results