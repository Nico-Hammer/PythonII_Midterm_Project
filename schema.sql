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

INSERT OR REPLACE INTO Products (product_id,name, price, stock_quantity) VALUES (1,'Pant', 25.99, 10);
INSERT OR REPLACE INTO Products (name, price, stock_quantity) VALUES ("laptop", 26.99, 500);
INSERT OR REPLACE INTO Electronics (product_id, warranty_period) VALUES (2, '2 years');
INSERT OR REPLACE INTO Products (name, price, stock_quantity) VALUES ("Milk", 3.99, 20);
INSERT OR REPLACE INTO Perishable (product_id, expiration_date) VALUES (3, '2024-12-31');
INSERT OR REPLACE INTO Sales (sale_id,product_id, quantity,total_sale,sale_date) VALUES (1,3, 5,15,'2026-03-03');