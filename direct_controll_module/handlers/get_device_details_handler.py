from rest_framework import status
from rest_framework.response import Response

from direct_controll_module.handlers.handler import Handler
from direct_controll_module.repositories.boolean_iot_device_repository import BooleanIotDeviceRepository
from direct_controll_module.serializers.boolean_iot_device_serializer import BooleanIotDeviceSerializer


class GetDeviceDetailsHandler(Handler):

    def __init__(self, request, device_id):
        super().__init__(request, device_id)
        self.device_repository = BooleanIotDeviceRepository()

    def handle(self, device_id):
        try:
            boolean_iot_device = self.device_repository.get_by_id(device_id)
        except ValueError:
            return Response(status=status.HTTP_404_NOT_FOUND)

        return Response(BooleanIotDeviceSerializer(boolean_iot_device).data)
