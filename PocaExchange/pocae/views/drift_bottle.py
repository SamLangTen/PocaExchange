from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pocae.models import *
from pocae.serializers import *
import uuid
import datetime

class DriftBottleList(APIView):

    def get(self, request, format=None):
        bottles = DriftBottle.objects.all()
        serializers = DriftBottleSerializer(bottles, many=True)
        return Response(serializers.data,status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = DriftBottleSerializer(data=request.data)
        if serializer.is_valid():
            bottle = DriftBottle(bottle_id=uuid.uuid4())
            bottle.request_name = User.objects.get(user_name=serializer.validated_data['request_name'])
            bottle.throw_time = datetime.datetime.now()
            bottle.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
