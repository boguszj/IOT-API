from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from ..handlers.create_device_handler import CreateDeviceHandler
from ..handlers.get_device_details_handler import GetDeviceDetailsHandler
from ..handlers.get_devices_hander import GetDevicesHandler
from ..handlers.set_device_state_handler import SetDeviceStateHandler


@api_view(http_method_names=['GET'])
def get_devices(request):
    return handle_view(GetDevicesHandler, request)


@api_view(http_method_names=['GET'])
def get_device_details(request, device_id):
    return handle_view(GetDeviceDetailsHandler, request, device_id)


@api_view(http_method_names=['POST'])
def create_device(request):
    return handle_view(CreateDeviceHandler, request)


@api_view(http_method_names=['PUT'])
def set_device_state(request, device_id):
    return handle_view(SetDeviceStateHandler, request, device_id)


def handle_view(handler, request, device_id=None):
    if request.META['preprocessing_status'] == '400':
        return Response(status=status.HTTP_400_BAD_REQUEST)
    elif request.META['preprocessing_status'] == '401':
        return Response(status=status.HTTP_401_UNAUTHORIZED)
    elif request.META['preprocessing_status'] == '500':
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    else:
        return handler(request, device_id).handle()





