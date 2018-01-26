from django.db import models

# Create your models here.

STATE_CHOICES = ((1, 'Unsent'), (2, 'Sent'), (3, 'Received'))


class PostcardPair(models.Model):
    pair_id = models.UUIDField(primary_key=True)
    sender = models.CharField(max_length=30)
    receiver = models.CharField(max_length=30)
    create_date = models.DateTimeField()
    send_date = models.DateTimeField(null=True)
    receive_date = models.DateTimeField(null=True)
    state = models.IntegerField(choices=STATE_CHOICES,default=1)
