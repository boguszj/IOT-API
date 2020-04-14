import uuid

from django.db import models


class BooleanIotDevice(models.Model):
    device_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(unique=True, max_length=50)
    state = models.BooleanField(default=False)

    class Meta:
        db_table = 'boolean_iot_device'
