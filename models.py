import db
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
    warranty_period: str

    def get_product_details(self):
        pass

@dataclass
class Perishable(Product):
    expiration_date: str

    def get_product_details(self):
        pass

@dataclass
class Sale:
    sale_id: int
    product_id: int
    quantity: int
    sale_date: str

    def reduce_stock(self,product_id,quantity):
        pass

    def calculate_total_sale(self,product_id,quantity):
        pass
    