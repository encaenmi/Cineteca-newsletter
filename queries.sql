CREATE TABLE cartelera (id INTEGER PRIMARY KEY, title STRING, year STRING, director STRING, created_at DATETIME DEFAULT CURRENT_TIMESTAMP);


CREATE TABLE cartelera (
    id INTEGER PRIMARY KEY, 
    title STRING, 
    year STRING, 
    director STRING, 
    created_at DATE DEFAULT (DATE('now'))
);

CREATE UNIQUE INDEX idx_unique_entry ON cartelera(title, year, director, created_at);

CREATE TABLE film_info (
    id INTEGER PRIMARY KEY, 
    adult BOOLEAN,
    backdrop_path STRING, 
    genre_ids STRING, 
    original_language STRING,
    original_title STRING, 
    overview STRING, 
    popularity REAL, 
    poster_path STRING, 
    release_date DATE, 
    title STRING, 
    video BOOLEAN, 
    vote_average REAL, 
    vote_count INTEGER,
    created_at DATE DEFAULT (DATE('now'))
);

ALTER TABLE cartelera ADD COLUMN showtime STRING;

CREATE TABLE subscribers (
    id INTEGER PRIMARY KEY,
    email STRING,
    created_at DATE DEFAULT (DATE('now'))
);