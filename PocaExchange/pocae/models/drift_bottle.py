from django.db import models
from django.contrib.auth.models import User
from pocae.models import *


class DriftBottle(models.Model):
    bottle_id = models.UUIDField(primary_key=True)
    request_name = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True)
    throw_time = models.DateTimeField()
    postcard_pair = models.OneToOneField(
        PostcardPair, on_delete=models.SET_NULL, null=True)
