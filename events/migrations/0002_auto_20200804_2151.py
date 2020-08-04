# Generated by Django 3.0.8 on 2020-08-04 19:51

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('events', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='eventattendee',
            unique_together={('event', 'user')},
        ),
    ]
