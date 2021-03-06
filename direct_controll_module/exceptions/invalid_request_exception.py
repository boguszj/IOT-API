class InvalidRequestException(Exception):

    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '[ERROR] Unexpected payload: ' + self.data
