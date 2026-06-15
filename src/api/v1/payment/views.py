from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.payment.serializers import BookingSerializer, RoomSerializer
from apps.payment.models import Bookings, Rooms
from config.settings import logger


class RoomApiView(APIView):
    def get(self, request, *args, **kwargs):
        rooms = Rooms.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(f"Room created: id={serializer.data['id']}, price={serializer.data['price']}")
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        room_id = kwargs.get("id")
        room = get_object_or_404(Rooms, id=room_id)
        room.delete()
        logger.warning(f"Room deleted: id={room_id}")
        return Response(status=204)


class BookingApiView(APIView):
    def get(self, request, *args, **kwargs):
        room_id = request.GET.get("room_id")
        bookings = Bookings.objects.filter(room_id=room_id)
        serializer = BookingSerializer(bookings, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = BookingSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        logger.info(
            f"Booking created: id={serializer.data['id']}, room={request.data.get('room_id')}, dates={request.data.get('start_date')}->{request.data.get('end_date')}"
        )
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        booking_id = kwargs.get("id")
        booking = get_object_or_404(Bookings, id=booking_id)
        booking.delete()
        logger.warning(f"Booking deleted: id={booking_id}")
        return Response(status=204)
