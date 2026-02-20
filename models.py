from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    stock_quantity: int

    def update_price(new_price):
        pass

    def update_stock(quantity):
        pass

    def is_in_stock(quantity):
        pass

    def sell(quantity):
        pass

    def get_product_details():
        pass

@dataclass
class Electronics(Product):
    warrany_period: int

    def get_product_details():
        pass

@dataclass
class Perishable(Product):
    expiration_date: str

    def get_product_details():
        pass

class Sale:
    def __init__(self,product,quantity):
        self.product = product
        self.quantity = quantity

    def reduct_stock():
        pass

    def calculate_total_sale():
        pass
    