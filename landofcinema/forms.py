from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['user','movie','theater','screen','seat_number','booking_date']
        #i have deciede to addthis i have lost my data fuck  