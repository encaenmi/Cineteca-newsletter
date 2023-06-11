import sqlite3
import json
from sqlite3 import Error


# wrapper for passing connections
def with_connection(func):

    def connection(*args, **kwargs):
        conn = sqlite3.connect("database.db")
        try:
            rv = func(conn, *args, **kwargs)
        except Error as e:
            conn.rollback()
            raise e
        else:
            conn.commit()
        finally:
            conn.close()
        return rv

    return connection


# get all in cartelera
@with_connection
def query_all(conn):
    query = "SELECT * FROM cartelera;"
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    return rows


# write to cartelera table
@with_connection
def write_to_cartelera(conn, info_list):
    try:
        c = conn.cursor()
        for info in info_list:
            # Insert a row of data
            c.execute(
                "INSERT OR IGNORE INTO cartelera (title, year, director, showtime) VALUES (?, ?, ?, ?)",
                (info['title'], info['year'], info['director'],
                 info['showtime']))
    except Error as e:
        print(e)


# store TMDB data
@with_connection
def write_api_data_to_db(conn, api_response):
    try:
        c = conn.cursor()
        for film in api_response['results']:
            # Extract data
            id = film['id']
            adult = film['adult']
            backdrop_path = film['backdrop_path']
            genre_ids = json.dumps(
                film['genre_ids'])  # store list as JSON string
            original_language = film['original_language']
            original_title = film['original_title']
            overview = film['overview']
            popularity = film['popularity']
            poster_path = film['poster_path']
            release_date = film['release_date']
            title = film['title']
            video = film['video']
            vote_average = film['vote_average']
            vote_count = film['vote_count']

            # Insert data into database
            c.execute(
                '''INSERT OR REPLACE INTO film_info (id, adult, backdrop_path, genre_ids, 
                original_language, original_title, overview, popularity, poster_path, 
                release_date, title, video, vote_average, vote_count) 
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                (id, adult, backdrop_path, genre_ids, original_language,
                 original_title, overview, popularity, poster_path,
                 release_date, title, video, vote_average, vote_count))

    except Error as e:
        print(e)
