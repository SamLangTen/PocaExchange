from django.db import models

# Create your models here.

class postcard_pair(models.Model):
    pair_id = models.UUIDField()
    sender = models.CharField(max_length = 30)
    receiver = models.CharField(max_length = 30)
    send_date = models.DateTimeField()
    receive_date = models.DateTimeField()
    state = models.IntegerField()