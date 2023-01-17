from django.contrib import admin
from .models import Movie, Theatre, Screen, Schedule, Users, Booking, Payment

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date')
    search_fields = ('title',)
    list_filter = ('release_date',)

class TheatreAdmin(admin.ModelAdmin):
    list_display = ('name', 'region', 'address')
    search_fields = ('name', 'region')
    list_filter = ('region',)

class ScreenAdmin(admin.ModelAdmin):
    list_display = ('theatre', 'screen_number', 'capacity')
    search_fields = ('theatre__name',)
    list_filter = ('theatre__region',)

class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('movie', 'screen', 'start_time', 'end_time')
    search_fields = ('movie__title', 'screen__theatre__name')
    list_filter = ('start_time', 'screen__theatre__region')
                   
class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', 'role')
    search_fields = ('username',)
    list_filter = ('role',)

class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'movie', 'theatre', 'screen', 'seat_number', 'booking_date')
    search_fields = ('user__username', 'movie__title', 'theatre__name')
    list_filter = ('booking_date', 'theatre__region')

class PaymentAdmin(admin.ModelAdmin):
    list_display = ('booking', 'amount', 'payment_date', 'status')
    search_fields = ('booking__user__username', 'booking__movie__title')
    list_filter = ('payment_date', 'status')

admin.site.register(Movie, MovieAdmin)
admin.site.register(Theatre, TheatreAdmin)
admin.site.register(Screen, ScreenAdmin)
admin.site.register(Schedule, ScheduleAdmin)
admin.site.register(Users, UsersAdmin)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Payment, PaymentAdmin)

