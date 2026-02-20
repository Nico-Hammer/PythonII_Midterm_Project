import sqlite3
from models import Product,Electronics,Perishable,Sale

def create_db():
    conn = sqlite3.connect("inventory.sqlite")
    with open("schema.sql") as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def connect():
    conn = sqlite3.connect('inventory.sqlite')
    conn.row_factory = sqlite3.Row
    conn.execute('PRAGMA foreign_keys = ON')
    return conn