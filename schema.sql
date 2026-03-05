CREATE TABLE IF NOT EXISTS Products(
     product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name TEXT NOT NULL,
     price REAL NOT NULL,
     stock_quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Electronics(
    product_id INTEGER PRIMARY KEY NOT NULL,
    warranty_period TEXT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Perishable(
    product_id INTEGER PRIMARY KEY NOT NULL,
    expiration_date TEXT NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Sales(
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    total_sale FLOAT NOT NULL,
    sale_date TEXT NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);  
