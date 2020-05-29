from django.core.exceptions import ObjectDoesNotExist

from direct_controll_module.exceptions.no_such_boolean_iot_device_exception import NoSuchBooleanIotDeviceException
from direct_controll_module.models.boolean_iot_device_model import BooleanIotDevice


class BooleanIotDeviceRepository:

    def get_by_id(self, device_id):
        try:
            return BooleanIotDevice.objects.get(device_id=device_id)
        except (ValueError, ObjectDoesNotExist):
            raise NoSuchBooleanIotDeviceException(device_id)

    def get_all(self):
        return BooleanIotDevice.objects.all()
