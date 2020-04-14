import uuid

from rest_framework import serializers
from ..models.boolean_iot_device_model import BooleanIotDevice


class BooleanIotDeviceSerializer(serializers.ModelSerializer):

    class Meta:
        model = BooleanIotDevice
        fields = ('device_id', 'name', 'state')

    def create(self, validated_data):
        boolean_iot_device = BooleanIotDevice(device_id=uuid.uuid4(), **validated_data)
        boolean_iot_device.save()
        return boolean_iot_device
