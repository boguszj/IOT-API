import json

import requests
import time
import jwt

from iot_api.settings import FB_APP_ID
from social_auth_module.exceptions.app_request_error import AppRequestError
from social_auth_module.exceptions.no_such_social_user import NoSuchFbUserException
from social_auth_module.models.fb_user_model import FbUserModel
from social_auth_module.repositories.fb_user_repository import SocialUserRepository


class FbUserValidator:

    def __init__(self, get_response):
        self.social_user_repository = SocialUserRepository()
        self.get_response = get_response

    def validate(self, request):
        [user_id, access_token, exp_date] = self.get_request_auth_data(request.headers['Authorization'])
        if not self.is_app_id_valid(self.get_app_id(access_token)):
            request.META['preprocessing_status'] = '400'
            return self.get_response(request)

        permissions = self.get_user_permissions(user_id)
        if not (((request.method == 'GET' and permissions == 'VIEW') or permissions == 'ALL') and self.verify_user(user_id, access_token, exp_date)):
            request.META['preprocessing_status'] = '401'
        else:
            request.META['preprocessing_status'] = None
        return self.get_response(request)

    def get_app_id(self, access_token):
        app_response = requests.get('https://graph.facebook.com/app?access_token=' + access_token)
        if not self.validate_response(app_response):
            raise AppRequestError()
        try:
            return json.loads(app_response.content)['id']
        except KeyError:
            return 'INVALID_APP_ID'

    def get_user_data(self, access_token):
        user_response = requests.get('https://graph.facebook.com/me?access_token=' + access_token)
        if not self.validate_response(user_response):
            raise AppRequestError()
        return {
            'id': json.loads(user_response.content)['id'],
            'name': json.loads(user_response.content)['name']
        }

    def verify_user(self, user_id, access_token, exp_date):
        return user_id == self.get_user_data(access_token)['id'] and exp_date > time.time() - 60

    def is_app_id_valid(self, app_id):
        return app_id == FB_APP_ID

    def get_user_permissions(self, user_id):
        try:
            user = self.social_user_repository.get_by_name(user_id)
        except NoSuchFbUserException:
            user = FbUserModel(name=user_id)
            user.save()
        return user.permissions


    def validate_response(self, response):
        return response.status_code != 200 or response.status_code != 404 or response.status_code != 400

    def get_request_auth_data(self, encoded_jwt):
        data = jwt.decode(encoded_jwt, 'SECRET', algorithms=['HS256'])
        return [data['userId'], data['token'], data['expirationDate']]
