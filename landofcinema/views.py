from django.shortcuts import render
from .models import Movie
from datetime import datetime, timezone
import requests
from .fetch_movies import fetch_and_save_movies


def index(request):
    """View function for home page of site."""

    # Call function to fetch and save movies
    movie_titles = ['matrix', 'avengers', 'jumanji']
    fetch_and_save_movies(movie_titles)

    # Retrieve the top 5 upcoming movies
    
    tz = timezone('Africa/Dar_es_Salaam')
    current_time = datetime.now(tz)
    upcoming_movies = Movie.objects.filter(release_date__gte=current_time).order_by('release_date')[:5]

    # Retrieve the top 5 highest rated movies
    highest_rated_movies = Movie.objects.order_by('-rating')[:5]

    context = {
        'upcoming_movies': upcoming_movies,
        'highest_rated_movies': highest_rated_movies,
    }

    return render(request, 'index.html', context)
