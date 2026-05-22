from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView

from api.v1.payment.serializers import RoomSerializer
from apps.payment.models import Rooms


class RoomApiView(APIView):
    def get(self, request, *args, **kwargs):
        rooms = Rooms.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = RoomSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def delete(self, request, *args, **kwargs):
        room_id = kwargs.get("id")
        room = get_object_or_404(Rooms, id=room_id)
        room.delete()
        return Response(status=204)
