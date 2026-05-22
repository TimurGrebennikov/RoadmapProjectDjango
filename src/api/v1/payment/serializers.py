from rest_framework import serializers

from apps.payment.models import Bookings, Rooms


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = ["id", "description", "price"]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookings
        fields = ["id", "room", "start_date", "end_date", "date_of_creation"]
