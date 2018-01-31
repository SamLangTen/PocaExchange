from rest_framework import serializers
from api.models import *

class PostcardPairSerializer(serializers.Serializer):
    pair_id = serializers.UUIDField(required=False)
    sender = serializers.CharField(max_length=30)
    receiver = serializers.CharField(max_length=30)
    send_date = serializers.DateTimeField(required=False)
    receive_date = serializers.DateTimeField(required=False)
    state = serializers.ChoiceField(choices=STATE_CHOICES)
