from django.http import Http404
from django.contrib.auth.models import *
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from api.models import *
from api.serializers import *
import uuid
import datetime


class DriftBottleList(APIView):

    @permission_classes((IsAdminUser, ))
    def get(self, request, format=None):
        bottles = DriftBottle.objects.all()
        serializers = DriftBottleSerializer(bottles, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)

    @permission_classes((IsAuthenticated, ))
    def post(self, request, format=None):       
        if not DriftBottle.objects.filter(request_name=request.user).exists():
            bottle = DriftBottle(bottle_id=uuid.uuid4())
            bottle.request_name = request.user
            bottle.throw_time = datetime.datetime.now()
            bottle.save()
            return Response(status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class DriftBottleDetail(APIView):

    def post(self, request, format=None):
        pass
