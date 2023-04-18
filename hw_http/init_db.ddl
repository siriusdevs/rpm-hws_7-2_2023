CREATE TABLE IF NOT EXISTS cities (id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY, city text, country text, language text, population int);

CREATE TABLE IF NOT EXISTS token (
    username text NOT NULL primary key,
    token uuid);
    
INSERT INTO token (username, token) VALUES ('admin', '537dc091-cbeb-4802-84f8-46f0ea57694c');