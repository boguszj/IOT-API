from rest_framework.response import Response

from direct_controll_module.models.boolean_iot_device_model import BooleanIotDevice
from direct_controll_module.repositories.boolean_iot_device_repository import BooleanIotDeviceRepository
from direct_controll_module.serializers.boolean_iot_device_serializer import BooleanIotDeviceSerializer


class GetDevicesHandler:

    def __init__(self):
        self.device_repository = BooleanIotDeviceRepository()

    def handle(self):
        boolean_iot_devices = []
        for boolean_iot_device in self.device_repository.get_all():
            boolean_iot_devices.append(boolean_iot_device)
        return Response(BooleanIotDeviceSerializer(boolean_iot_devices, many=True).data)
