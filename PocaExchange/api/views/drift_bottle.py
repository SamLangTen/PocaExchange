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
import random


class DriftBottleList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAdminUser,)

    def get(self, request, format=None):
        bottles = DriftBottle.objects.all()
        serializers = DriftBottleSerializer(bottles, many=True)
        return Response(serializers.data, status=status.HTTP_200_OK)


class DriftBottlePoolList(APIView):
    authentication_classes = (SessionAuthentication, BasicAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request, format=None):
        '''
            Drift Bottle Thrown
        '''
        bottles_own = DriftBottle.objects.filter(request_name=request.user)
        bottles_accepted = bottles_own.exclude(postcard_pair=None)
        bottles_unreceived = bottles_accepted.exclude(
            postcard_pair=PostcardPair.objects.filter(sender=request.user, state=3))
        if (not bottles_own.exists()) or (bottles_unreceived.exists()):
            bottle = DriftBottle(bottle_id=uuid.uuid4())
            bottle.request_name = request.user
            bottle.throw_time = datetime.datetime.now()
            bottle.save()
            return Response(data={"bottle_id": bottle.bottle_id}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)

    def put(self, request, format=None):
        '''
            Drift Bottle Dragged
        '''
        bottles_unown = DriftBottle.objects.exclude(request_name=request.user)
        bottles_accepted = bottles_unown.exclude(postcard_pair=None)
        bottles_unreceived = bottles_accepted.filter(
            postcard_pair=PostcardPair.objects.filter(receiver=request.user).exclude(state=3))
        if not bottles_unreceived.exists():
            bottles_unaccepted = bottles_unown.filter(postcard_pair=None)
            bottle_index = random.randint(0, bottles_unaccepted.count()-1)
            bottle_selected = bottles_unaccepted[bottle_index]
            pc_pair = PostcardPair(pair_id=uuid.uuid4())
            pc_pair.sender = bottle_selected.request_name
            pc_pair.receiver = request.user
            pc_pair.create_date = datetime.datetime.now()
            pc_pair.save()
            bottle_selected.postcard_pair = pc_pair
            bottle_selected.save()
            return Response(data={"bottle_id": bottle_selected.bottle_id, "postcard_pair_id": pc_pair.pair_id}, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)


class DriftBottleDetail(APIView):

    def post(self, request, format=None):
        pass
