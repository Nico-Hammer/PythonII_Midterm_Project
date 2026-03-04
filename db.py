import sqlite3

def create_db():
    conn = sqlite3.connect("inventory.db")
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def connect():
    conn = sqlite3.connect('inventory.db')
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

## PRODUCT QUERIES ##
def get_all_products():
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Products")
        return c.fetchall()

def get_product_by_id(id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Products WHERE product_id = ?",(id,))
        return c.fetchone()

def add_product(product_id,name,price,stock_quantity):
    with connect() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Products(product_id,name,price,stock_quantity) VALUES(?,?,?,?)",(product_id,name,price,stock_quantity))
        conn.commit()

def delete_product(product_id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM Products WHERE product_id = ?",(product_id,))
        conn.commit()

def update_price(product_id,new_price):
    with connect() as conn:
        c = conn.cursor()
        c.execute("UPDATE Products SET price = ? WHERE product_id = ?",(new_price,product_id))
        conn.commit()

def update_stock(product_id,new_stock):
    with connect() as conn:
        c = conn.cursor()
        c.execute("UPDATE Products SET stock_quantity = ? WHERE product_id = ?",(new_stock,product_id))
        conn.commit()

## ELECTRONIC QUERIES ##
def get_all_electronics():
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Electronics")
        return c.fetchall()

def get_electronic_by_id(id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Electronics WHERE product_id = ?",(id,))
        return c.fetchone()

def add_electronic(product_id,warranty_period):
    with connect() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Electonics(product_id,warranty_period) VALUES(?,?)",(product_id,warranty_period))
        conn.commit()

## PERISHABLE QUERIES ##
def get_all_perishables():
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Perishable")
        return c.fetchall()

def get_perishable_by_id(id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Perishable WHERE product_id = ?",(id,))
        return c.fetchone()
        
def add_perishable(product_id,expiration_date):
    with connect() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Perishable(product_id,expiration_date) VALUES(?,?)",(product_id,expiration_date))
        conn.commit()

## SALE QUERIES ##
def get_all_sales():
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Sales")
        return c.fetchall()

def get_sale_by_id(id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("SELECT * FROM Sales WHERE sale_id = ?",(id,))
        return c.fetchone()
        
def add_sale(sale_id,product_id,quantity,total_sale,sale_date):
    with connect() as conn:
        c = conn.cursor()
        c.execute("INSERT INTO Sales(sale_id,product_id,quantity,total_sale,sale_date) VALUES(?,?,?,?,?)",(sale_id,product_id,quantity,total_sale,sale_date))
        conn.commit()

def update_sale(sale_id,new_quantity,new_total):
    with connect() as conn:
        c = conn.cursor()
        c.execute("UPDATE Sales SET quantity = ?, total_sale = ? WHERE sale_id = ?",(new_quantity,new_total,sale_id))
        conn.commit()

def delete_sale(sale_id):
    with connect() as conn:
        c = conn.cursor()
        c.execute("DELETE FROM Sales WHERE sale_id = ?",(sale_id,))
        conn.commit()