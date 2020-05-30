from direct_controll_module.handlers.preprocessing_status_handlers.PreprocessingStatusHandlingStrategy import \
    PreprocessingStatusHandlingStrategy
from rest_framework import status
from rest_framework.response import Response


class PreprocessingStatusInternalErrorHandler(PreprocessingStatusHandlingStrategy):
    def __init__(self, handler):
        super().__init__(handler)

    def applies(self, meta_status):
        return meta_status == '500'

    def handle(self):
        return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

