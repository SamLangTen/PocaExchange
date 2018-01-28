from rest_framework import serializers
from pocae.models import *
import uuid
import datetime

class DriftBottleSerializer(serializers.Serializer):
    bottle_id = serializers.UUIDField()
    request_name = serializers.CharField(max_lenth=100,required=False)
    throw_time = serializers.DateTimeField()
    postcard_pair_id = serializers.UUIDField(required=False)

    def to_representation(self, instance):
        self.bottle_id = instance.bottle_id
        self.request_name = instance.request_name
        self.throw_time = instance.throw_time
        self.postcard_pair_id = instance.postcard_pair.pair_id

    def create(self, validated_data):
        bottle = DriftBottle()
        bottle.bottle_id = uuid.uuid4()
        bottle.throw_time = datetime.datetime.now()
        bottle.request_name = User.objects.get(user_id=validated_data['request_name'])
        bottle.postcard_pair = PostcardPair.objects.get(pair_id=validated_data['postcard_pair_id'])
        return bottle.save()

    def update(self, instance, validated_data):
        instance.bottle_id = validated_data['bottle_id']
        instance.throw_time = validated_data['throw_time']
        instance.request_name = User.objects.get(user_id=validated_data['request_name'])
        instance.postcard_pair = PostcardPair.objects.get(pair_id=validated_data['postcard_pair_id'])
        instance.save()
        return instance