# gui goes here
import tkinter as tk
from inventory import Inventory
from models import Product, Electronics, Perishable, Sale

inventory = Inventory()

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("500x400")

def add_product():
    add_window = tk.Toplevel(root)
    add_window.title("Add Product")
    add_window.geometry("300x300")

    tk.Label(add_window, text="Product ID").pack()
    id_entry = tk.Entry(add_window)
    id_entry.pack()

    tk.Label(add_window, text="Name").pack()
    name_entry = tk.Entry(add_window)
    name_entry.pack()

    tk.Label(add_window, text="Price").pack()
    price_entry = tk.Entry(add_window)
    price_entry.pack()

    tk.Label(add_window, text="Stock Quantity").pack()
    stock_entry = tk.Entry(add_window)
    stock_entry.pack()

    def submit():
        try:
            product_id = int(id_entry.get())
            name = name_entry.get()
            price = float(price_entry.get())
            stock = int(stock_entry.get())

            product = Product(product_id, name, price, stock)
            inventory.add_product(product)

            print("Product added successfully")
            add_window.destroy()

        except Exception as e:
            print("Error:", e)

    tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

def remove_product():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Product")
    remove_window.geometry("300x300")

    tk.Label(remove_window, text="Product ID").pack()
    id_entry = tk.Entry(remove_window)
    id_entry.pack()

    def submit():
        try:
            product_id = int(id_entry.get())

            inventory.remove_product(product_id)
            print(f"Product {product_id} removed successfully")
            remove_window.destroy()

        except Exception as e:
            print("Error:", e)
    
    tk.Button(remove_window, text="Submit", command=submit).pack(pady=10)

def list_products():
    list_window = tk.Toplevel(root)
    list_window.title("List Products")
    list_window.geometry("300x300")

    products = inventory.list_products()

    for product in products:
        tk.Label(list_window, text=f"ID: {product.product_id}, Name: {product.name}, Price: {product.price}, Stock: {product.stock_quantity}").pack()

def sell_product():
    list_window = tk.Toplevel(root)
    list_window.title("Sell Product")
    list_window.geometry("300x300")

    tk.Label(list_window, text="Sell Product selected").pack()

def restock_product():
    print("Restock Product selected")

tk.Button(root, text="Add Product", command=add_product).pack(pady=10)
tk.Button(root, text="Remove Product", command=remove_product).pack(pady=10)    
tk.Button(root, text="List Products", command=list_products).pack(pady=10)
tk.Button(root, text="Sell Product", command=sell_product).pack(pady=10)
tk.Button(root, text="Restock Product", command=restock_product).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
