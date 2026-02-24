CREATE TABLE IF NOT EXISTS Products(
     product_id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     name TEXT NOT NULL,
     price REAL NOT NULL UNIQUE,
     stock_quantity INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS Electronics(
    product_id INTEGER NOT NULL,
    warranty_period TEXT NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL UNIQUE,
    stock_quantity INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Perishables(
    product_id INTEGER NOT NULL,
    expiration_date TEXT NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL UNIQUE,
    stock_quantity INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE 
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS SALES(
    sale_id INTEGER PRIMARY KEY,
    product_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    FOREIGN KEY (product_id) REFERENCES Products(product_id)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);  

INSERT INTO Products (name, price, stock_quantity) VALUES ('Pant', 25.99, 10);
INSERT INTO Electronics (name, price, stock_quantity, warranty_period) VALUES ("laptop", 26.99, 500,'2 years');
INSERT INTO Perishables (name, price, stock_quantity, expiration_date) VALUES ("Milk", 3.99, 20, '2024-12-31');
INSERT INTO SALES (product_id, quantity) VALUES (3, 5);