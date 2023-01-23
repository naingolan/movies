from django.urls import path

from landofcinema.forms import BookingForm, ScheduleForm
from . import views
from .views import *


urlpatterns = [
    path('', views.index, name="index"),
]
urlpatterns += [
    #These are for the normal user 
    path('book_seats/', views.book_seats, name='book_seats'),
    path('book_seats/<int:schedule_id>/', views.book_seats, name='book_seat'),
    path('view_bookings/', views.view_bookings, name='view_bookings'),

    
    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
    path('payment/', views.Payment, name='payment'),
    path('search/', views.search_schedules, name='search_schedules'),
    path('create_showing_time/', views.create_showing_time, name='create_showing_time'),
    path('view_schedule/',views.schedule_view, name='view_schedule'),
    
    
    #These are for  the employee
    path('add_schedule/', views.schedule_create, name='schedule'),
    path('add_movie/', views.add_movie, name='addmovies'),
    
    #This applies for both 
    path('register/', views.register, name='register'),
    
]
