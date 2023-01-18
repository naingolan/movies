from datetime import datetime

import requests

from landofcinema.models import Movie

def fetch_and_save_movies(titles):
    for title in titles:
        # Make an API request to omdb
        response = requests.get(f'http://www.omdbapi.com/?apikey=f8ccb335&t={title}')

        # Convert the response to a Python dictionary
        movie_data = response.json()

        # Extract the movie data from the dictionary
        title = movie_data['Title']
        synopsis = movie_data['Plot']
        released_date = datetime.strptime(movie_data['Released'], '%d %b %Y').strftime('%Y-%m-%d')
        image_url = movie_data['Poster']

        # Create a new Movie object and save it to the database
        movie = Movie(title=title, synopsis=synopsis, release_date=released_date, image_url=image_url)
        movie.save()
