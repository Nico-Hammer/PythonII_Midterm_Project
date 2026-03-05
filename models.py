import db
from datetime import datetime
from dataclasses import dataclass

@dataclass
class Product:
    product_id: int
    name: str
    price: float
    stock_quantity: int

    def update_price(self,new_price):
        db.update_price(self.product_id,new_price)

    def update_stock(self,new_quantity):
        db.update_stock(self.product_id,new_quantity)

    def is_in_stock(self):
        stock = db.get_stock(self.product_id)
        if(stock > 0):
            return True
        else:
            return False

    def sell(self,quantity):
        stock = db.get_stock(self.product_id)
        new_stock = stock - quantity
        db.update_stock(self.product_id,new_stock)

    def get_product_details(self):
        return f"-----\nID: {self.product_id}\nName: {self.name}\nPrice: {self.price}\nStock: {self.stock_quantity}\n-----"

@dataclass
class Electronics(Product):
    warranty_period: str

    def get_product_details(self):
        return f"-----\nID: {self.product_id}\nName: {self.name}\nPrice: {self.price}\nStock: {self.stock_quantity}\nWarranty: {self.warranty_period}\n-----"

@dataclass
class Perishable(Product):
    expiration_date: str

    def get_product_details(self):
        return f"-----\nID: {self.product_id}\nName: {self.name}\nPrice: {self.price}\nStock: {self.stock_quantity}\Expiration: {self.expiration_date}\n-----"

@dataclass
class Sale:
    sale_id: int
    product_id: int
    quantity: int
    total_sale: float
    sale_date: str

    def reduce_stock(self,product_id,quantity):
        stock = db.get_stock(product_id)
        new_stock = stock - quantity
        db.update_stock(self.product_id,new_stock)
        total_sale = self.calculate_total_sale(self.sale_id,product_id,quantity)
        sale_date  = datetime.today().strftime('%Y-%m-%d')
        db.add_sale(self.sale_id,product_id,quantity,total_sale,sale_date)

    def calculate_total_sale(self,product_id,quantity):
        product_price = db.get_price(product_id)
        total = product_price * quantity
        return total
    