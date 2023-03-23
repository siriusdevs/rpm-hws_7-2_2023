CREATE TABLE IF NOT EXISTS students(
    id serial,
    fname text NOT NULL,
    lname text NOT NULL,
    sname text, 
    group_ text NOT NULL,
    age int
);

CREATE TABLE IF NOT EXISTS professors(
    id serial,
    fname text NOT NULL,
    patronymic text NOT NULL,
    lname text,
    subject text,
    age int
);

CREATE TABLE IF NOT EXISTS trees(
    id serial,
    tree text NOT NULL,
    height int,
    age int NOT NULL,
    yield int
);

CREATE EXTENSION "uuid-ossp";
CREATE TABLE token (
    username TEXT PRIMARY KEY,
    token uuid
);
INSERT INTO token VALUES ('admin', 'a1b2c3d4-a1b2-c3d4-e5f6-a1b2c3a1b2c3');