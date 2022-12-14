DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS manufacturers;


CREATE TABLE manufacturers (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    shipping_speed VARCHAR(255),
    status BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    size INT,
    stock_quantity INT,
    buying_cost INT,
    selling_price INT,
    manufacturer_id INT NOT NULL REFERENCES manufacturers(id) ON DELETE CASCADE
);

