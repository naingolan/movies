from django.forms import ModelForm
from .models import Booking

class BookingForm(ModelForm):
    class Meta:
        model = Booking
        fields = ['movie','theater','screen','seat_number','booking_date']
        #i have deciede to addthis i have lost my data fuck  

from .models import Schedule

class ScheduleForm(ModelForm):
    class Meta:
        model = Schedule
        fields = ['movie', 'screen', 'start_time', 'end_time']

from django import forms

class PaymentForm(forms.Form):
    booking = forms.IntegerField()
    amount = forms.FloatField()
    payment_date = forms.DateTimeField()
    status = forms.CharField(max_length=255)



from django import forms
from .models import *

class ShowingTimeForm(forms.Form):
    movie = forms.ModelChoiceField(queryset=Movie.objects.all())
    theater = forms.ModelChoiceField(queryset=Theater.objects.all())
    screen = forms.ModelChoiceField(queryset=Screen.objects.all())
    start_time = forms.DateTimeField()
    end_time = forms.DateTimeField()
    
    
    
#This is for adding movies 
class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'synopsis', 'release_date', 'image_url', 'rating']
        
        
        
#for registering

from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

def save(self, commit=True):
    user = super(CustomUserCreationForm, self).save(commit=False)
    user.email = self.cleaned_data["email"]
    if commit:
        user.save()
    return user