import db
from models import Product, Electronics, Perishable

class Inventory:
    # Add a product to the inventory
    def add_product(self, product):
        product_id = db.add_product(
            None,
            product.name, 
            product.price, 
            product.stock_quantity
        )
        if isinstance(product, Electronics):
            db.add_electronic(product_id, product.warranty_period)
        elif isinstance(product, Perishable):
            db.add_perishable(product_id, product.expiration_date)


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
            product_id = row['product_id']
            name = row['name']
            price = row['price']
            stock_quantity = row['stock_quantity']

            e_row = db.get_electronic_by_id(product_id)
            if e_row:
                products.append(Electronics(product_id, name, price, stock_quantity, e_row['warranty_period']))
                continue

            p_row = db.get_perishable_by_id(product_id)
            if p_row:
                products.append(Perishable(product_id, name, price, stock_quantity, p_row['expiration_date']))
                continue
            
            products.append(Product(product_id, name, price, stock_quantity))
        return products
    
    def sell_product(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product and product.is_in_stock() and product.stock_quantity >= quantity:
            product.sell(quantity)
            return True
        else:
            return False
    