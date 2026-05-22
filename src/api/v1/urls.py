from django.urls import path

from .payment import views

urlpatterns = [
    path("rooms/", views.RoomApiView.as_view(), name="rooms-list"),
    path("rooms/create/", views.RoomApiView.as_view(), name="rooms-create"),
    path("rooms/delete/<int:id>/", views.RoomApiView.as_view(), name="rooms-delete"),
    path("bookings/create/", views.BookingApiView.as_view(), name="booking-create"),
    path("bookings/delete/<int:id>/", views.BookingApiView.as_view(), name="booking-delete"),
    path("bookings/list/", views.BookingApiView.as_view(), name="booking-list"),
]
