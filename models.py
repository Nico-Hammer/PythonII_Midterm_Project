from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    stock_quantity: int

    def update_price(self,new_price):
        pass

    def update_stock(self,quantity):
        pass

    def is_in_stock(self,quantity):
        pass

    def sell(self,quantity):
        pass

    def get_product_details():
        pass

@dataclass
class Electronics(Product):
    warranty_period: int

    def get_product_details(self):
        pass

@dataclass
class Perishable(Product):
    expiration_date: str

    def get_product_details(self):
        pass

class Sale:
    def __init__(self,product,quantity):
        self.product = product
        self.quantity = quantity

    def reduce_stock(self,product,quantity):
        pass

    def calculate_total_sale(self,product,quantity):
        pass
    