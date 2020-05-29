from rest_framework import status
from rest_framework.response import Response

from direct_controll_module.handlers.handler import Handler
from direct_controll_module.serializers.boolean_iot_device_serializer import BooleanIotDeviceSerializer


class CreateDeviceHandler(Handler):

    def __init__(self, request):
        super().__init__(request)

    def handle(self):

        data = self.request.data
        if isinstance(self.request.data, str):
            data = {'name': self.request.data}

        serializer = BooleanIotDeviceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['device_id'], status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)