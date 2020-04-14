class NoSuchBooleanIotDeviceException(Exception):

    def __init__(self, device_id):
        self.device_id = device_id

    def __str__(self):
        return 'No device with id: ' + self.device_id
