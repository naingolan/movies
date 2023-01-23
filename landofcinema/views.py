from django.shortcuts import render
from .models import Booking, Movie, Schedule
from datetime import datetime, timezone
import requests
from .fetch_movies import fetch_and_save_movies
import pytz

def index(request):
    """View function for home page of site."""
    # Call function to fetch and save movies
    movie_titles = ['puss in boots', 'avatar', 'jumanji', 'inception', ]
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
from django.contrib.auth.decorators import login_required

@login_required
def book_seats(request, schedule_id):
    schedule = Schedule.objects.get(pk=schedule_id)
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.schedule = schedule
            booking.save()
            return redirect('index')
    else:
        form = BookingForm()
    return render(request, 'book_seats.html', {'form': form, 'schedule': schedule})

#creating a view for schedule
from django.shortcuts import render, redirect
from .forms import ScheduleForm

def schedule_create(request):
    if not request.user.is_authenticated:
        return redirect('index')
    if not request.user.groups.filter(name='employees').exists():
        return redirect('index')
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            schedule = form.save()
            return redirect('add_schedule', pk=schedule.pk)
    else:
        form = ScheduleForm()
    return render(request, 'add_schedule.html', {'form': form})



#Viewing shedule
from django.views.generic import ListView
from .models import Schedule, Theater, Movie

class ScheduleListView(ListView):
    model = Schedule
    template_name = 'schedule_list.html'
    context_object_name = 'schedules'

    def get_queryset(self):
        return Schedule.objects.prefetch_related('screen__theater', 'movie')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['theaters'] = Theater.objects.all()
        context['movies'] = Movie.objects.all()
        return context


#confirm payment schedule
from django.shortcuts import render
from .forms import PaymentForm
from .models import Payment
from django.shortcuts import render, get_object_or_404

def confirm_payment(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            payment_date = form.cleaned_data['payment_date']
            status = form.cleaned_data['status']
            Payment.objects.create(booking=booking, amount=amount, payment_date=payment_date, status=status)
    else:
        form = PaymentForm()
    return render(request, 'confirm_payment.html', {'form': form, 'booking': booking})




#This is  for movie, shcedules and theater search 
from .models import Schedule, Movie, Theater

def search_schedules(request):
    query = request.GET.get('q')
    schedules = None
    movies = None
    theaters = None
    if query:
        schedules = Schedule.objects.filter(movie__title__icontains=query)
        movies = Movie.objects.filter(title__icontains=query)
        theaters = Theater.objects.filter(name__icontains=query)
    return render(request, 'search_schedules.html', {'schedules': schedules, 'movies': movies, 'theaters': theaters})



#Payment preview 
from django.shortcuts import render, redirect
from .models import Payment, Booking
from .forms import PaymentForm
from . import models

def payment(request, booking_id):
    #booking = get_object_or_404(Booking, id=booking_id)
    #booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    booking = Booking.objects.get(id=booking_id)
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            payment = form.save(commit=False)
            payment.booking = booking
            payment.save()
            return redirect('payment_success')
    else:
        form = PaymentForm()
    return render(request, 'payment.html', {'form': form, 'booking': booking})




# creating a view which will authenticate a user and allow him to enter details 
from django.contrib.auth.decorators import user_passes_test
from .models import *

def is_employee(user):
    try:
        employee = Employee.objects.get(user=user)
        if employee.role == 'showing_times_loader':
            return True
        else:
            return False
    except Employee.DoesNotExist:
        return False
    
    
    
    
from django.shortcuts import render, redirect
from .forms import ShowingTimeForm

@user_passes_test(is_employee)

def create_showing_time(request):
    if request.method == 'POST':
        form = ShowingTimeForm(request.POST)
        if form.is_valid():
            movie = form.cleaned_data.get('movie')
            theater = form.cleaned_data.get('theater')
            screen = form.cleaned_data.get('screen')
            start_time = form.cleaned_data.get('start_time')
            end_time = form.cleaned_data.get('end_time')
            
            schedule = Schedule.objects.create(
                movie=movie,
                theater=theater,
                screen=screen,
                start_time=start_time,
                end_time=end_time
            )
            schedule.save()
            
            return redirect('showing_time_success')
    else:
        form = ShowingTimeForm()
    return render(request, 'create_showing_time.html', {'form': form})



#Adding new movie by the user 
from django.shortcuts import render, redirect
from .forms import MovieForm
from django.contrib.auth.models import Group

def add_movie(request):
    if not request.user.groups.filter(name='Employee').exists():
        return redirect('index')
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = MovieForm()
    return render(request, 'add_movie.html', {'form': form})


#this is for displaying the movies 
from django.shortcuts import render
from .models import Schedule, Theater, Movie, Screen

# def schedule_view(request):
#     schedules = Schedule.objects.all()
#     theaters = Theater.objects.all()
#     movies = Movie.objects.all()
#     screens = Screen.objects.all()
#     context = {
#         'schedules': schedules,
#         'theaters': theaters,
#         'movies': movies,
#         'screens': screens
#     }
#     return render(request, 'schedule.html', context)

def schedule_view(request):
    schedules = Schedule.objects.all()
    theaters = Theater.objects.all()
    return render(request, 'schedule.html', {'schedules': schedules, 'theaters': theaters})


#registering  new users 
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, authenticate

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})


#checking user bookings 
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Booking
@login_required
def view_bookings(request):
    if request.user.is_authenticated:
        bookings = Booking.objects.filter(user=request.user)
        return render(request, 'view_bookings.html', {'bookings': bookings})
    else:
        return redirect('login')
