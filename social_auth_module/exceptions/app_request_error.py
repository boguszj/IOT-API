class AppRequestError(Exception):

    def __init__(self):
        pass

    def __str__(self):
        return 'Error verifing request'
