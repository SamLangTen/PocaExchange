from rest_framework import serializers
from pocae.models import *
import uuid
import hashlib

class UserCreationSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(required=False)
    user_name = serializers.CharField(max_length=100)
    password = serializers.CharField(max_length=100)
    user_group = serializers.ChoiceField(choices=USER_GROUP_TYPES)

    def create(self, validated_data):
        validated_data['user_id'] = uuid.uuid4()
        validated_data['password'] = hashlib.sha256().update(validated_data['password'].encode('utf-8').hexdigest())
        return User.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.user_id = validated_data.get('user_id',instance.user_id)
        instance.user_name = validated_data.get('user_name',instance.user_name)
        instance.password = hashlib.sha256().update(validated_data['password'].encode('utf-8').hexdigest())
        instance.save()
        return instance

class UserSerializer(serializers.Serializer):
    user_id = serializers.UUIDField(required=False)
    user_name = serializers.CharField(max_length=100)
    user_group = serializers.ChoiceField(choices=USER_GROUP_TYPES)

