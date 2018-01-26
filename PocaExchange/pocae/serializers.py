from rest_framework import serializers
from pocae.models import *
import uuid
import datetime

class PostcardPairSerializer(serializers.Serializer):
    pair_id = serializers.UUIDField(required=False)
    sender = serializers.CharField(max_length=30)
    receiver = serializers.CharField(max_length=30)
    send_date = serializers.DateTimeField(required=False)
    receive_date = serializers.DateTimeField(required=False)
    state = serializers.ChoiceField(choices=STATE_CHOICES)

    def create(self, validated_data):
        validated_data['pair_id'] = uuid.uuid4()
        validated_data['create_date'] = datetime.datetime.now()
        return PostcardPair.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.send_date = validated_data.get(
            'send_date', instance.send_date)
        instance.receive_date = validated_data.get(
            'receive_date', instance.receive_date)
        instance.state = validated_data.get('state', instance.state)
        instance.save()
        return instance
