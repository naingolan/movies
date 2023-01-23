from django.db import models
from dateutil.parser import parse
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    synopsis = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    image_url = models.URLField()
    rating = models.FloatField(default=0.0)

    def save(self, *args, **kwargs):
        if self.release_date:
            self.release_date = parse(self.release_date).date()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class Theater(models.Model):
    name = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Screen(models.Model):
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    screen_number = models.IntegerField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"{self.theater} - Screen {self.screen_number}"

class Schedule(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.movie} - {self.screen} - {self.start_time} - {self.end_time}"

from django.contrib.auth.models import User

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    theater = models.ForeignKey(Theater, on_delete=models.CASCADE)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE)
    seat_number = models.CharField(max_length=255)
    booking_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user} - {self.movie} - {self.theater} - {self.screen} - {self.seat_number} - {self.booking_date}"

class Payment(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_date = models.DateTimeField()
    status = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.booking} - {self.amount} - {self.payment_date} - {self.status}"


#This is for adding employee
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_employee = models.BooleanField(default=False)


from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import UserProfile

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
