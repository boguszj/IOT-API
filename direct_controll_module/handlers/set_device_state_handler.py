from rest_framework import status
from rest_framework.response import Response
from direct_controll_module.exceptions.iot_notification_exception import IotNotificationException
from direct_controll_module.handlers.handler import Handler
from direct_controll_module.notifiers.boolean_iot_device_state_change_notifier import BooleanIotDeviceStateChangeNotifier
from direct_controll_module.repositories.boolean_iot_device_repository import BooleanIotDeviceRepository, NoSuchBooleanIotDeviceException


class SetDeviceStateHandler(Handler):

    def __init__(self, request, device_id):
        super().__init__(request, device_id)
        self.device_repository = BooleanIotDeviceRepository()
        self.notifier = BooleanIotDeviceStateChangeNotifier()

    def handle(self):
        try:
            boolean_iot_device = self.device_repository.get_by_id(self.device_id)
        except NoSuchBooleanIotDeviceException:
            return Response(status=status.HTTP_404_NOT_FOUND)

        boolean_iot_device.state = self.request.data['state']

        try:
            self.notifier.notify_iot(boolean_iot_device)
        except IotNotificationException:
            return Response(status=status.HTTP_501_INTERNAL_SERVER_ERROR)

        boolean_iot_device.save()

        return Response("Update successful", status.HTTP_202_ACCEPTED)
