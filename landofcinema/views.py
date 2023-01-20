from django.shortcuts import render
from .models import Booking, Movie, Schedule
from datetime import datetime, timezone
import requests
from .fetch_movies import fetch_and_save_movies
import pytz

def index(request):
    """View function for home page of site."""
    # Call function to fetch and save movies
    movie_titles = ['matrix', 'avengers', 'jumanji', 'inception', ]
    for title in movie_titles:
        response = requests.get(f'http://www.omdbapi.com/?apikey=f8ccb335&t={title}')
        movie_data = response.json()

        # Extract the movie data from the dictionary
        title = movie_data['Title']
        synopsis = movie_data['Plot']
        released_date = movie_data['Released']
        image_url = movie_data['Poster']

        # Create a new Movie object and save it to the database
        movie = Movie(title=title, synopsis=synopsis, release_date=released_date, image_url=image_url)
        movie.save()

    # Retrieve the top 5 upcoming movies
    tz = pytz.timezone('Africa/Dar_es_Salaam')
    current_time = datetime.now(tz)
    upcoming_movies = Movie.objects.filter(release_date__gte=current_time).order_by('release_date')[:5]

    # Retrieve the top 5 highest rated movies
    highest_rated_movies = Movie.objects.order_by('-rating')[:5]

    movies = Movie.objects.all()
    context = {
        'upcoming_movies': upcoming_movies,
        'highest_rated_movies': highest_rated_movies,
        'movies': movies
    }

    return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from .forms import BookingForm

def book_seats(request):
    booking = Booking.objects.get(pk=1)
    if request.method == 'POST':
        form = BookingForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('book_seats')
    else:
        form = BookingForm(instance=booking)
    return render(request, 'book_seats.html', {'form': form})

#creating a view for schedule
from django.shortcuts import render, redirect
from .forms import ScheduleForm

def schedule_create(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return redirect('add_schedule', pk=schedule.pk)
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})
