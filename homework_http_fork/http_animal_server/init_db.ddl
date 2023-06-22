CREATE TABLE IF NOT EXISTS animals (id int PRIMARY KEY GENERATED ALWAYS AS IDENTITY, kind text, areal text, fact text);

CREATE TABLE IF NOT EXISTS token (
    username text NOT NULL primary key,
    token uuid);
    
INSERT INTO token (username, token) VALUES ('admin', 'fe705453-aec1-408b-af94-556910ca0651');

insert INTO animals (kind, areal, fact)
values ('Lion', 'Africa', 'king'),
     ('Elephant', 'Africa', 'large'),
     ('Penguin', 'Antarctica', 'swimmer'),
     ('Alpaca', 'South America', 'valuable wool'),
     ('Whale', 'Pacific Ocean', 'mammal'),
     ('Wolf', 'North America', 'predator');