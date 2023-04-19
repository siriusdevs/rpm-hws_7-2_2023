CREATE EXTENSION IF NOT EXISTS "uuid-ossp";

CREATE TABLE IF NOT EXISTS token (
    username text NOT NULL primary key,
    token uuid
);

INSERT INTO token (username, token) VALUES ('admin', '92a33179-87f3-43fb-9f18-ffdb63289c66');

CREATE TABLE IF NOT exists coins (
  id int generated always as identity primary key,
  token_name VARCHAR(255),
  approximate_price DECIMAL(10, 2),
  status text not NULL,
  listing_date DATE
);

insert into coins (token_name, approximate_price, status, listing_date) 
VALUES 
   ('FMilk', 88.30, 'Upcoming', '2023-11-12'),
   ('Grizz', 2.50, 'Active', '2022-04-04'),
   ('Xorn', 90.00, 'Upcoming', '2023-02-11');