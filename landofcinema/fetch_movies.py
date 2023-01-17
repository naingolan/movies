import requests
from .models import Movie

# Make an API request to omdb
response = requests.get('http://www.omdbapi.com/?apikey=f8ccb335&t=matrix')

# Convert the response to a Python dictionary
movie_data = response.json()

# Extract the movie data from the dictionary
title = movie_data['Title']
synopsis = movie_data['Plot']
released_date = movie_data['Released']
image_url = movie_data['Poster']

# Create a new Movie object and save it to the database
movie = Movie(title=title, synopsis=synopsis, released_date=released_date, image_url=image_url)
movie.save()
