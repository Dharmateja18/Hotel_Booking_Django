from django.db import models
from django.contrib.auth.models import User
import datetime
# Create your models here.

class Amenities(models.Model):
    amenity_name = models.CharField(max_length=100)

    def __str__(self):
        return self.amenity_name

class Hotel(models.Model):
    hotel_name = models.CharField(max_length=100)
    hotel_price = models.IntegerField()
    description = models.TextField(default='no details')
    amenities = models.ManyToManyField(Amenities)
    room_count = models.IntegerField(default=10)

    def __str__(self):
        return self.hotel_name

class HotelImages(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    images = models.ImageField(upload_to='hotels')

    def __str__(self):
        return f"{self.hotel.hotel_name} Image"

class HotelBooking(models.Model):
    hotel = models.ForeignKey(Hotel, related_name="hotel_bookings", on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name="user_bookings", on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    booking_type = models.CharField(max_length=100, choices=(('Pre Paid', 'Pre Paid'), ('Post Paid', 'Post Paid')))
    STATUS_CHOICES = (
    ('Pending', 'Pending'),
    ('Accepted', 'Accepted'),
    ('Rejected', 'Rejected'),
    )

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')


    def __str__(self):
        return f"{self.user.username} - {self.hotel.hotel_name} ({self.start_date} to {self.end_date})"
