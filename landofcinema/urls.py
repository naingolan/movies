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
    path('view_schedule/',views.schedule_view, name='view_schedule'),

    
    # path('schedules/', ScheduleListView.as_view(), name='schedule_list'),
    path('confirm_payment/', views.confirm_payment, name='confirm_payment'),
    path('payment/', views.Payment, name='payment'),
    path('search/', views.search_schedules, name='search_schedules'),
    path('create_showing_time/', views.create_showing_time, name='create_showing_time'),
   
    
    #These are for  the employee
    path('add_schedule/', views.add_schedule, name='schedule'),
    path('delete_shedule/<int:schedule_id>/', views.schedule_delete, name='delete_schedule'),
    path('schedule_list', views.schedule_list, name='schedule_list_admin'),
    path('edit_schedule/<int:schedule_id>/', views.schedule_edit, name='schedule_edit_admin'),
    
    path('add_movie/', views.add_movie, name='addmovies'),
    path('edit_movie/<int:movie_id>/', views.edit_movie, name='edit_movie'),
    path('delete_movie/<int:movie_id>/', views.delete_movie, name='delete_movie'),
    path('movies_list', views.movies_list, name="movies_list"),
    
    
    
    #This applies for both 
    path('register/', views.register, name='register'),
    
]
