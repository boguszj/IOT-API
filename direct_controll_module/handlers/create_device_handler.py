from rest_framework import status
from rest_framework.response import Response

from direct_controll_module.serializers.boolean_iot_device_serializer import BooleanIotDeviceSerializer


class CreateDeviceHandler:

    def handle(self, request):

        data = request.data
        if isinstance(request.data, str):
            data = {'name': request.data}

        serializer = BooleanIotDeviceSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data['device_id'], status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)