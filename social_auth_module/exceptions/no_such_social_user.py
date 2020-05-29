class NoSuchFbUserException(Exception):

    def __init__(self, social_id):
        self.social_id = social_id

    def __str__(self):
        return 'No facebook user with id: ' + self.social_id
