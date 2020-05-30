from rest_framework.decorators import api_view

from ..handlers.create_device_handler import CreateDeviceHandler
from ..handlers.get_device_details_handler import GetDeviceDetailsHandler
from ..handlers.get_devices_hander import GetDevicesHandler
from ..handlers.preprocessing_status_handlers.PreprocessingStatusBadRequestHandler import \
    PreprocessingStatusBadRequestHandler
from ..handlers.preprocessing_status_handlers.PreprocessingStatusHandlingStrategy import \
    PreprocessingStatusHandlingStrategy
from ..handlers.preprocessing_status_handlers.PreprocessingStatusInternalErrorHandler import \
    PreprocessingStatusInternalErrorHandler
from ..handlers.preprocessing_status_handlers.PreprocessingStatusSuccessHandler import PreprocessingStatusSuccessHandler
from ..handlers.preprocessing_status_handlers.PreprocessingStatusUnauthorizedHandler import \
    PreprocessingStatusUnauthorizedHandler
from ..handlers.set_device_state_handler import SetDeviceStateHandler


@api_view(http_method_names=['GET'])
def get_devices(request):
    return handle_view(GetDevicesHandler(request, None), request)


@api_view(http_method_names=['GET'])
def get_device_details(request, device_id):
    return handle_view(GetDeviceDetailsHandler(request, device_id), request)


@api_view(http_method_names=['POST'])
def create_device(request):
    return handle_view(CreateDeviceHandler(request), request)


@api_view(http_method_names=['PUT'])
def set_device_state(request, device_id):
    return handle_view(SetDeviceStateHandler(request, device_id), request)


def handle_view(handler, request):
    strategies = [
        PreprocessingStatusBadRequestHandler(handler),
        PreprocessingStatusInternalErrorHandler(handler),
        PreprocessingStatusUnauthorizedHandler(handler),
        PreprocessingStatusSuccessHandler(handler)
    ]
    return PreprocessingStatusHandlingStrategy(handler).handle_startegy(request.META['preprocessing_status'], strategies)





