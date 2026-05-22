from django.db import models


class Rooms(models.Model):
    description: models.TextField = models.TextField()
    price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)


class Bookings(models.Model):
    room: models.ForeignKey = models.ForeignKey(Rooms, on_delete=models.CASCADE)
    end_date: models.DateField = models.DateField()
    start_date: models.DateField = models.DateField()
    date_of_creation: models.DateField = models.DateField(auto_now_add=True)
