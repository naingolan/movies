from django.urls import path

from landofcinema.forms import BookingForm
from . import views

urlpatterns = [
    path('', views.index, name="index"),
]

urlpatterns += [
    path('book_seats/', views.book_seats, name='booking_form'),
]
