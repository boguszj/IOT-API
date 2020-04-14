from rest_framework.decorators import api_view

from ..handlers.create_device_handler import CreateDeviceHandler
from ..handlers.get_device_details_handler import GetDeviceDetailsHandler
from ..handlers.get_devices_hander import GetDevicesHandler
from ..handlers.set_device_state_handler import SetDeviceStateHandler


@api_view(http_method_names=['GET'])
def get_devices(request):
    return GetDevicesHandler().handle()


@api_view(http_method_names=['GET'])
def get_device_details(request, device_id):
    return GetDeviceDetailsHandler().handle(device_id)


@api_view(http_method_names=['POST'])
def create_device(request):
    return CreateDeviceHandler().handle(request)


@api_view(http_method_names=['PUT'])
def set_device_state(request, device_id):
    return SetDeviceStateHandler().handle(request, device_id)





