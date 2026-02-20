CREATE TABLE IF NOT EXISTS Products(
     product_id INTEGER PRIMARY KEY AUTOINCREMENT,
     name TEXT NOT NULL,
     price REAL NOT NULL UNIQUE
     stock_quantity INTEGER NOT NULL
)

CREATE TABLE IF NOT EXISTS Electronics(
     product_id INTEGER PRIMARY KEY,
     warranty_period TEXT NOT NULL,
     FOREIGN KEY(product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
)

CREATE TABLE IF NOT EXISTS Perishables(
    product_id INTEGER PRIMARY KEY,
    expiration_date TEXT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
)

CREATE TABLE IF NOT EXISTS SALES() -- not done yet