from rest_framework import serializers

class DriftBottleSerializer(serializers.Serializer):
    bottle_id = serializers.UUIDField(required=False)
    request_name = serializers.CharField(max_length=100,required=False)
    throw_time = serializers.DateTimeField(required=False)
    postcard_pair_id = serializers.UUIDField(required=False)
