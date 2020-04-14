import requests

from direct_controll_module.exceptions.iot_notification_exception import IotNotificationException
from iot_api.settings import WEB_SERVER_ADDRESS


class BooleanIotDeviceStateChangeNotifier:

    def notify_iot(self, boolean_iot_device):
        name = boolean_iot_device.name
        state = boolean_iot_device.state
        resp = None
        try:
            resp = requests.post(WEB_SERVER_ADDRESS + name + '/' + str(state))
        except (requests.exceptions.Timeout, requests.exceptions.ConnectionError):
            pass
        if resp is None or resp.status_code != 200:
            print('[ERROR] Could not notify iot')
            raise IotNotificationException()
