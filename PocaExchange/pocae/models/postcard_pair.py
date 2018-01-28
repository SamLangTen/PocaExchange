from django.db import models
from pocae.models import *

# Create your models here.

STATE_CHOICES = ((1, 'Unsent'), (2, 'Sent'), (3, 'Received'))


class PostcardPair(models.Model):
    pair_id = models.UUIDField(primary_key=True)
    sender = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='postcard_sent_by_this_user')
    receiver = models.ForeignKey(User,on_delete=models.SET_NULL,null=True,related_name='postcard_received_by_this_user')
    create_date = models.DateTimeField()
    send_date = models.DateTimeField(null=True)
    receive_date = models.DateTimeField(null=True)
    state = models.IntegerField(choices=STATE_CHOICES,default=1)
