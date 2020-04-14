class IotNotificationException(Exception):

    def __str__(self):
        return 'Could not notify iot device'
