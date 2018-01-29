from django.db import models

USER_GROUP_TYPES = [(1, 'Administrator'), (2, 'Exchanger')]


class User(models.Model):
    user_id = models.UUIDField(primary_key=True)
    user_name = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    user_group = models.IntegerField(choices=USER_GROUP_TYPES, default=2)
