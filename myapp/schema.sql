DROP TABLE IF EXISTS jokes;

CREATE TABLE jokes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    url VARCHAR NOT NULL,
    value TEXT NOT NULL
);