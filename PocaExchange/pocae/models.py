from django.db import models

# Create your models here.

STATE_CHOICES = ((1,'Sending'),(2,'Sent'),(3,'Received'))

class PostcardPair(models.Model):
    pair_id = models.UUIDField()
    sender = models.CharField(max_length = 30)
    receiver = models.CharField(max_length = 30)
    send_date = models.DateTimeField()
    receive_date = models.DateTimeField()
    state = models.IntegerField(choices=STATE_CHOICES)