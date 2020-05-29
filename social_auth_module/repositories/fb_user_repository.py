from django.core.exceptions import ObjectDoesNotExist

from social_auth_module.exceptions.no_such_social_user import NoSuchFbUserException
from social_auth_module.models.fb_user_model import FbUserModel


class SocialUserRepository:

    def get_by_name(self, name):
        try:
            return FbUserModel.objects.get(name=name)
        except (ValueError, ObjectDoesNotExist):
            raise NoSuchFbUserException(name)
