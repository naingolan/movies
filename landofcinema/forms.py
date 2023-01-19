from django import forms
class BookingForm(forms.Form):
    movie_title = forms.CharField(max_length=255)
    theater_name = forms.CharField(max_length=255)
    show_date = forms.DateField()
    no_of_seats = forms.IntegerField()
    email = forms.EmailField()
    phone_number = forms.CharField(max_length=255)
