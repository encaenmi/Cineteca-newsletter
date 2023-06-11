import requests
import re
import os
import json
from bs4 import BeautifulSoup
from datetime import datetime
from db_functions import *

TMDB_KEY = os.environ['TMDB_KEY']
TMDB_BASE_URL = "https://api.themoviedb.org/3/"
OLD_CINETECA_URL = "https://www.cinetecanacional.net/controlador.php?opcion=carteleraDia"
NEW_CINETECA_URL = "https://www.cinetecanacional.net/cartelera.php"

RATING_WEIGHT = 0.7
VOTES_WEIGHT = 0.3

# Get today's films from Cineteca
#     Store in DB
# For each film, get info from TMDB using title and year
#     Store every result in DB
# For each first result, format and add to text
# Send email with text

# TODO
# Add trailer link
# Classify films in time categories (e.g. evening)
# Add picks for times?
# Add picks for other categories?
# Get films for the whole weekend
# Schedule to run on Friday morning
# Ensure cartelera has one row per scheduled slot


# get today's films from the cineteca
# would take date in ISO format (2023-06-11)
def get_cineteca_films(date=""):
    url = NEW_CINETECA_URL
    if date != "":
        url += f"?dia={date}"

    response = requests.get(url)

    if response.status_code != 200:
        print("Failed to get info")

    content = response.content
    soup = BeautifulSoup(content, "html.parser")
    """
    # old version
    elements = soup.find_all(class_="peliculaMiniFicha")
    inner_texts = [element.text for element in elements]
    """
    # new version (for changes made before 2023-06-07)
    elements = soup.select('.col-12.col-md-6.col-lg-4.float-left .small')
    inner_texts = [el.text for el in elements]

    return inner_texts


# extract title, director, year and showtime from cineteca info
def extract_info(films):
    film_info_list = []

    # Step of 2 to take both film and its corresponding showtime
    for i in range(0, len(films), 2):
        film_info = {}

        film = films[i]
        # Extract the film's title
        title_search = re.search('\((.*?),', film)
        if title_search:
            film_info['title'] = title_search.group(1)

        # Extract the director's name
        director_search = re.search('Dir\.\: (.*?),', film)
        if director_search:
            film_info['director'] = director_search.group(1)

        # Extract the film's year
        year_search = re.search('\, (.*?), Dur', film)
        if year_search:
            # Split the countries and year by comma, then extract the last element (year)
            year_country = year_search.group(1).split(',')
            film_info['year'] = int(year_country[-1].strip())

        # Extract the film's showtime from the next element in the list
        if i + 1 < len(films):  # Ensure we're not exceeding list bounds
            showtime_info = films[i + 1]
            showtime_search = re.search('\SALA \d+\: (.*?)\\n', showtime_info)
            if showtime_search:
                film_info['showtime'] = showtime_search.group(1)

        if film_info:  # If the dict isn't empty, append to the list
            film_info_list.append(film_info)

    return film_info_list


def get_film_TMDB_info(title, year=""):
    url = TMDB_BASE_URL + f"search/movie?query={title}&include_adult=false"

    if year != "":
        # url += f"&primary_release_year={year}"
        url += f"&year={year}"

    headers = {"accept": "application/json", "Authorization": TMDB_KEY}

    response = requests.get(url, headers=headers)

    return json.loads(response.content)


def film_score(rating, votes, min_rating, max_rating, min_votes, max_votes):
    r = (rating - min_rating) / (max_rating - min_rating)
    v = (votes - min_votes) / (max_votes - min_votes)
    return r * RATING_WEIGHT + v * VOTES_WEIGHT


def main():

    target_date = datetime.now().date().isoformat()

    # Get films currently showing
    inner_texts = get_cineteca_films(target_date)

    # Extract relevant info
    film_info = extract_info(inner_texts)

    # adds date to showtime, should probably improve
    for i in film_info:
        i["showtime"] = target_date + " " + i["showtime"]

    # Write to DB
    write_to_cartelera(film_info)

    info_for_text = []
    # Loop over every film in cartelera
    for film in film_info:
        # Get all TMDB results for title and year
        TMDB_results = get_film_TMDB_info(film["title"], film["year"])

        # Write TMDB results in film_info table
        write_api_data_to_db(TMDB_results)

        if len(TMDB_results["results"]) > 0:
            # Get the first TMDB result
            first_result = TMDB_results["results"][0]

            info_for_text.append({
                # cineteca info
                "cineteca_title": film["title"],
                "cineteca_director": film["director"],
                "cineteca_year": film["year"],
                "cineteca_showtime": film["showtime"],
                # TMDB info
                "result_title": first_result["title"],
                "release_date": first_result["release_date"],
                "rating": first_result["vote_average"],
                "popularity": first_result["popularity"],
                "overview": first_result["overview"],
                "votes": first_result["vote_count"]
            })
        else:
            info_for_text.append({
                # cineteca info
                "cineteca_title": film["title"],
                "cineteca_director": film["director"],
                "cineteca_year": film["year"]
            })

    # Compute the minimum and maximum ratings and votes for normalization
    min_rating = min(film.get('rating', 0) for film in info_for_text)
    max_rating = max(film.get('rating', 0) for film in info_for_text)
    min_votes = min(film.get('votes', 0) for film in info_for_text)
    max_votes = max(film.get('votes', 0) for film in info_for_text)

    sorted_films = sorted(
        info_for_text,
        key=lambda x: film_score(x.get("rating", 0), x.get("votes", 0),
                                 min_rating, max_rating, min_votes, max_votes),
        reverse=True)

    print(sorted_films)
