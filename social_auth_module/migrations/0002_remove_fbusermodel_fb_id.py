# Generated by Django 3.0.5 on 2020-05-12 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('social_auth_module', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='fbusermodel',
            name='fb_id',
        ),
    ]