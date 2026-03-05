# gui goes here
import tkinter as tk
from tkinter import messagebox
from inventory import Inventory
from models import Product, Electronics, Perishable, Sale
import db
from datetime import datetime

inventory = Inventory()

root = tk.Tk()
root.title("Inventory Management System")
root.geometry("500x500")

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

        # Show the correct label and entry
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
            messagebox.showerror("Invalid input", "Invalid price or stock. Please enter numeric values.")
            return
        
        if type_var.get() == "Electronics":
            product = Electronics(None, name, price, stock_quantity, int(warranty_entry.get()))
        elif type_var.get() == "Perishable":
            try:
                exp_date = parse_date(expiration_entry.get())
            except ValueError:
                messagebox.showerror("Invalid date", "Invalid date format. Use YYYY-MM-DD.")
                return
            product = Perishable(None, name, price, stock_quantity, exp_date)
        else:
            product = Product(None, name, price, stock_quantity)

        inventory.add_product(product)
        messagebox.showinfo("Product Added", f"Product {name} added successfully")
        add_window.destroy()

    tk.Button(add_window, text="Submit", command=submit).pack(pady=10)

def remove_product():
    remove_window = tk.Toplevel(root)
    remove_window.title("Remove Product")
    remove_window.geometry("300x300")

    tk.Label(remove_window, text="Enter Product ID").pack()
    id_entry = tk.Entry(remove_window)
    id_entry.pack()

    def submit():
        try:
            product_id = int(id_entry.get())
            # Check existence first
            product = inventory.get_product_by_id(product_id)
            if product is None:
                messagebox.showerror("Not found", f"Product with ID {product_id} does not exist.")
                return
            inventory.remove_product(product_id)
            messagebox.showinfo("Product Removed", f"Product {product_id} removed successfully")
            remove_window.destroy()

        except ValueError:
            messagebox.showerror("Invalid input", "Enter a valid product ID.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    
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
    sell_window = tk.Toplevel(root)
    sell_window.title("Sell Product")
    sell_window.geometry("300x300")

    tk.Label(sell_window, text="Enter Product ID").pack()
    id_entry = tk.Entry(sell_window)
    id_entry.pack()

    tk.Label(sell_window, text="Enter amount to be sold").pack()
    quantity_entry = tk.Entry(sell_window)
    quantity_entry.pack()

    def submit():
        try:
            product_id = int(id_entry.get())
            quantity = int(quantity_entry.get())
            product = inventory.get_product_by_id(product_id)
            if product is None:
                messagebox.showerror("Not found", "Product not found.")
                return
            if not product.is_in_stock():
                messagebox.showerror("Out of stock", "Product is out of stock.")
                return
            if quantity > product.stock_quantity:
                messagebox.showerror("Insufficient stock", "Not enough stock available.")
                return
            product.sell(quantity)
            messagebox.showinfo("Sale Complete", f"Sold {quantity} of product {product_id}.")
            sell_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid input", "Enter valid product ID and quantity.")

    tk.Button(sell_window, text="Submit", command=submit).pack(pady=10)



def restock_product():
    restock_window = tk.Toplevel(root)
    restock_window.title("Restock Product")
    restock_window.geometry("300x300")

    tk.Label(restock_window, text="Enter Product ID").pack()
    id_entry = tk.Entry(restock_window)
    id_entry.pack()

    tk.Label(restock_window, text="Enter restock amount").pack()
    quantity_entry = tk.Entry(restock_window)
    quantity_entry.pack()

    def submit():
        try:
            product_id = int(id_entry.get())
            quantity = int(quantity_entry.get())
            product = inventory.get_product_by_id(product_id)
            if product is None:
                messagebox.showerror("Not found", "Product not found.")
                return
            new_stock = product.stock_quantity + quantity
            product.update_stock(new_stock)
            messagebox.showinfo("Restocked", f"Restocked {quantity} of product {product_id}. New stock: {new_stock}.")
            restock_window.destroy()
        except ValueError:
            messagebox.showerror("Invalid input", "Enter valid product ID and quantity.")

    tk.Button(restock_window, text="Submit", command=submit).pack(pady=10)

def exit_app():
    root.quit()

tk.Button(root, text="Add Product", command=add_product).pack(pady=10)
tk.Button(root, text="Remove Product", command=remove_product).pack(pady=10)    
tk.Button(root, text="List Products", command=list_products).pack(pady=10)
tk.Button(root, text="Sell Product", command=sell_product).pack(pady=10)
tk.Button(root, text="Restock Product", command=restock_product).pack(pady=10)
tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
