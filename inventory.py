class Inventory:
    pass

class Inventory:
    def __init__(self):
        # Stores products using product_id as key
        self.products = {}

    # Add a product to inventory
    def add_product(self, product):
        self.products[product.product_id] = product

    # Remove a product from inventory
    def remove_product(self, product_id):
        if product_id in self.products:
            del self.products[product_id]

    # Get a product by its ID
    def get_product(self, product_id):
        return self.products.get(product_id)

    # List all products in inventory
    def list_products(self):
        return list(self.products.values())