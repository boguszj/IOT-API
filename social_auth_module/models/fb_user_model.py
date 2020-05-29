import uuid

from django.db import models


class FbUserModel(models.Model):
    user_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50)
    permissions = models.CharField(max_length=50, default='NONE')

    class Meta:
        db_table = 'fb_user'
