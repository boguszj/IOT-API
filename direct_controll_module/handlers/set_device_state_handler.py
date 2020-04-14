from rest_framework import status
from rest_framework.response import Response
from direct_controll_module.exceptions.invalid_request_exception import InvalidRequestException
from direct_controll_module.exceptions.iot_notification_exception import IotNotificationException
from direct_controll_module.notifiers.boolean_iot_device_state_change_notifier import BooleanIotDeviceStateChangeNotifier
from direct_controll_module.repositories.boolean_iot_device_repository import BooleanIotDeviceRepository, NoSuchBooleanIotDeviceException


class SetDeviceStateHandler:

    def __init__(self):
        self.device_repository = BooleanIotDeviceRepository()
        self.notifier = BooleanIotDeviceStateChangeNotifier()

    def handle(self, request, device_id):
        try:
            self.verify_request(request)
        except InvalidRequestException:
            return Response("Expected values: ['true', 'false']", status.HTTP_400_BAD_REQUEST)
        try:
            boolean_iot_device = self.device_repository.get_by_id(device_id)
        except NoSuchBooleanIotDeviceException:
            return Response(status=status.HTTP_404_NOT_FOUND)

        boolean_iot_device.state = self.get_logical_value(request)

        try:
            self.notifier.notify_iot(boolean_iot_device)
        except IotNotificationException:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        boolean_iot_device.save()

        return Response("Update successful", status.HTTP_202_ACCEPTED)

    def get_logical_value(self, request):
        return True if request.data['state'] == 'true' else False

    def verify_request(self, request):
        if request.data['state'] not in ['true', 'false']:
            raise InvalidRequestException(request.data)
