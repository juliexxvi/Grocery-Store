SELECT 'CREATE DATABASE grocery_store' WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'grocery_store') \gexec

\c grocery_store

DROP TABLE IF EXISTS products;
CREATE TABLE products (
  id serial PRIMARY KEY,
  name text NOT NULL,
  image_url text,
  price_in_cents integer NOT NULL,
  brand text,
  store text NOT NULL,
  code text NOT NULL,
  cup_price text,
  package_size text
);

DROP TABLE IF EXISTS orders;
CREATE TABLE orders (
  id serial PRIMARY KEY,
  customer_name text NOT NULL,
  customer_address text NOT NULL,
  total_amount integer NOT NULL
);

DROP TABLE IF EXISTS order_details;
CREATE TABLE order_details (
  id serial PRIMARY KEY,
  order_id integer REFERENCES orders(id),
  product_id integer REFERENCES products(id),
  quantity integer NOT NULL,
  unit_price_in_cents integer NOT NULL
);

DROP TABLE IF EXISTS users;
CREATE TABLE users(
  id serial PRIMARY KEY, 
  email text NOT NULL, 
  name text NOT NULL,
  password_hash text NOT NULL,
  role text NOT NULL
);
