from datetime import date

from django.test import TestCase
from rest_framework.test import APIClient

from apps.payment.models import Bookings, Rooms


class RoomsAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.room = Rooms.objects.create(description="Тестовый номер", price=10000)
        self.booking = Bookings.objects.create(
            room=self.room,
            start_date=date(2025, 1, 10),
            end_date=date(2025, 1, 15),
            date_of_creation=date.today(),
        )

    def test_create_room(self):
        response = self.client.post(
            "/api/v1/rooms/create/", {"description": "Люкс", "price": 15000}
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Rooms.objects.count(), 2)
        self.assertEqual(response.data["description"], "Люкс")  # type: ignore
        self.assertEqual(response.data["price"], "15000.00")  # type: ignore

    def test_get_rooms(self):
        response = self.client.get("/api/v1/rooms/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # type: ignore

    def test_delete_room(self):
        response = self.client.delete(f"/api/v1/rooms/delete/{self.room.id}/")  # type: ignore
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Rooms.objects.count(), 0)

    def test_create_booking(self):
        response = self.client.post(
            "/api/v1/bookings/create/",
            {"room": self.room.id, "start_date": "2025-02-01", "end_date": "2025-02-05"},  # type: ignore
        )
        self.assertEqual(response.status_code, 201)

    def test_get_bookings(self):
        response = self.client.get(f"/api/v1/bookings/list/?room_id={self.room.id}")  # type: ignore
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)  # type: ignore

    def test_delete_booking(self):
        response = self.client.delete(f"/api/v1/bookings/delete/{self.booking.id}/")  # type: ignore
        self.assertEqual(response.status_code, 204)
        self.assertEqual(Bookings.objects.count(), 0)
