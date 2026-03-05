# gui goes here
import tkinter as tk
from inventory import Inventory
from models import Product, Electronics, Perishable, Sale
import db
from datetime import datetime

inventory = Inventory()

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("500x400")

def add_product():
    add_window = tk.Toplevel(root)
    add_window.title("Add Product")
    add_window.geometry("300x350")

    name_entry = tk.Entry(add_window); tk.Label(add_window, text="Name").pack(); name_entry.pack()
    price_entry = tk.Entry(add_window); tk.Label(add_window, text="Price").pack(); price_entry.pack()
    stock_entry = tk.Entry(add_window); tk.Label(add_window, text="Stock").pack(); stock_entry.pack()

    type_var = tk.StringVar(value="Regular")
    tk.Label(add_window, text="Type").pack()
    tk.OptionMenu(add_window, type_var, "Regular", "Electronics", "Perishable").pack()

    warranty_label = tk.Label(add_window, text="Warranty for Electronics (Months)")
    warranty_entry = tk.Entry(add_window)

    expiration_label = tk.Label(add_window, text="Expiration for Perishables (YYYY-MM-DD)")
    expiration_entry = tk.Entry(add_window)

    def parse_date(date_str):
        for fmt in ('%Y-%m-%d', '%Y %m %d', '%Y/%m/%d'):
            try:
                dt = datetime.strptime(date_str, fmt)
                return dt.strftime('%Y-%m-%d')
            except ValueError:
                continue
        raise ValueError("Invalid date format.")     

    # Function to show/hide fields based on product type
    def update_fields(*args):
        # Hide everything first
        warranty_label.pack_forget()
        warranty_entry.pack_forget()
        expiration_label.pack_forget()
        expiration_entry.pack_forget()

        # Show the correct label + entry
        if type_var.get() == "Electronics":
            warranty_label.pack()
            warranty_entry.pack()
        elif type_var.get() == "Perishable":
            expiration_label.pack()
            expiration_entry.pack()

    type_var.trace_add("write", update_fields)

    def submit():
        name = name_entry.get()
        try: 
            price = float(price_entry.get())
            stock_quantity = int(stock_entry.get())
        except: 
            print("Invalid input"); 
            return
        
        if type_var.get() == "Electronics":
            product = Electronics(None, name, price, stock_quantity, int(warranty_entry.get()))
        elif type_var.get() == "Perishable":
            try:
                exp_date = parse_date(expiration_entry.get())
            except ValueError:
                print("Invalid date format. Use YYYY-MM-DD.")
                return
            product = Perishable(None, name, price, stock_quantity, exp_date)
        else:
            product = Product(None, name, price, stock_quantity)

        inventory.add_product(product)
        print(f"Product {name} added successfully")
        add_window.destroy()

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

        except ValueError:
            print("Invalid input. Enter a valid product ID.")
        except Exception as e:
            print("Error:", e)
    
    tk.Button(remove_window, text="Submit", command=submit).pack(pady=10)

def list_products():
    list_window = tk.Toplevel(root)
    list_window.title("All Products")
    list_window.geometry("300x300")

    text_area = tk.Text(list_window)
    text_area.pack(fill=tk.BOTH, expand=True)

    products = inventory.list_products()

    if len(products) == 0:
        text_area.insert(tk.END, "No products in inventory.\n")
    else:
        for p in products:
            details = f"ID: {p.product_id}\nName: {p.name}\nPrice: {p.price}\nStock: {p.stock_quantity}"

            if isinstance(p, Electronics):
                details += f"\nWarranty: {p.warranty_period}"
            elif isinstance(p, Perishable):
                details += f"\nExpiration: {p.expiration_date}"
            details += "\n----------------------\n"
            text_area.insert(tk.END, details)

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
