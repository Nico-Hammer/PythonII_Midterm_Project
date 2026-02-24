CREATE TABLE IF NOT EXISTS Products(
     product_id INTEGER PRIMARY KEY NOT NULL,
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
    FOREIGN KEY(product_id) REFERENCES Products(product_id),
    FOREIGN KEY (name) REFERENCES Products(name),
    FOREIGN KEY (price) REFERENCES Products(price),
    FOREIGN KEY (stock_quantity) REFERENCES Products(stock_quantity)
    ON DELETE CASCADE
    ON UPDATE CASCADE
);

CREATE TABLE IF NOT EXISTS Perishables(
    product_id INTEGER NOT NULL,
    expiration_date TEXT NOT NULL,
    name TEXT NOT NULL,
    price REAL NOT NULL UNIQUE,
    stock_quantity INTEGER NOT NULL,
    FOREIGN KEY(product_id) REFERENCES Products(product_id),
    FOREIGN KEY (name) REFERENCES Products(name),
    FOREIGN KEY (price) REFERENCES Products(price),
    FOREIGN KEY (stock_quantity) REFERENCES Products(stock_quantity)
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

INSERT INTO Products (product_id,name, price, stock_quantity) VALUES (1,'Pant', 25.99, 10);
INSERT INTO Electronics (product_id,name, price, stock_quantity, warranty_period) VALUES (2,"laptop", 26.99, 500,'2 years');
INSERT INTO Perishables (product_id,name, price, stock_quantity, expiration_date) VALUES (3,"Milk", 3.99, 20, '2024-12-31');
INSERT INTO SALES (product_id, quantity) VALUES (3, 5);