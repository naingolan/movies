from django.urls import path

from landofcinema.forms import BookingForm
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]

from .views import book_seats

urlpatterns = [
    path('book/<int:movie_id>/', BookingForm, name='booking_form'),
]
