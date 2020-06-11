from social_auth_module.exceptions.app_request_error import AppRequestError
from social_auth_module.validators.fb_user_validator import FbUserValidator


class RequestAuthPreprocessor:

    def __init__(self, get_response):
        self.fb_user_validator = FbUserValidator(get_response)

    def __call__(self, request):
        try:
            if request.META.get('PATH_INFO', None) == '/swagger':
                print('aaa')
                return request
            else:
                return self.fb_user_validator.validate(request)
        except AppRequestError:
            request.META['preprocessing_status'] = '500'
            return self.fb_user_validator.get_response(request)


