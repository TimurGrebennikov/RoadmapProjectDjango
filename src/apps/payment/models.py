from django.db import models


class Rooms(models.Model):
    class Meta:
        app_label = "payment"

    description: models.TextField = models.TextField()  # type: ignore
    price: models.DecimalField = models.DecimalField(max_digits=10, decimal_places=2)  # type: ignore
    created_at: models.DateTimeField = models.DateTimeField(auto_now_add=True)  # type: ignore


class Bookings(models.Model):
    class Meta:
        app_label = "payment"

    room: models.ForeignKey = models.ForeignKey(Rooms, on_delete=models.CASCADE)  # type: ignore
    start_date: models.DateField = models.DateField()  # type: ignore
    end_date: models.DateField = models.DateField()  # type: ignore
    date_of_creation: models.DateField = models.DateField(auto_now_add=True)  # type: ignore
