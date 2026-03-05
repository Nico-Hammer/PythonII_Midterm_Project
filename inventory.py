import db
from models import Product, Electronics, Perishable

class Inventory:
    # Add a product to the inventory
    def add_product(self, product):
        db.add_product(
            product.product_id, 
            product.name, 
            product.price, 
            product.stock_quantity
        )
        if isinstance(product, Electronics):
            db.add_electronic(product.product_id, product.warranty_period)
        elif isinstance(product, Perishable):
            db.add_perishable(product.product_id, product.expiration_date)


    # Remove a product from the inventory
    def remove_product(self, product_id):
        db.delete_product(product_id)

    # Get a product by its ID
    def get_product_by_id(self, product_id):
        row = db.get_product_by_id(product_id)
        if row:
            return Product(row['product_id'], row['name'], row['price'], row['stock_quantity'])
        else:
            return None

    # List all products in inventory
    def list_products(self):
        rows = db.get_all_products()
        products = []
        for row in rows:
            products.append(Product(row['product_id'], row['name'], row['price'], row['stock_quantity']))
        return products