from django.urls import path
from .views.boolean_iot_device_view import get_device_details, create_device, get_devices, set_device_state

urlpatterns = [
    path('', get_devices),
    path('create/', create_device),
    path('<device_id>/update', set_device_state),
    path('<device_id>/', get_device_details)
]
