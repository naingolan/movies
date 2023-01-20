from django.urls import path

from landofcinema.forms import BookingForm, ScheduleForm
from . import views
from .views import ScheduleListView


urlpatterns = [
    path('', views.index, name="index"),
]
urlpatterns += [
    path('book_seats/', views.book_seats, name='booking_form'),
    path('add_schedule/', views.schedule_create, name='schedule'),
    path('schedules/', ScheduleListView.as_view(), name='schedule_list'),

]
