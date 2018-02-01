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

    def get(self, request, format=None):
        '''
            Get all bottles thrown and dragged
        '''
        bottles_own = DriftBottle.objects.filter(request_name=request.user)
        bottles_myaccepted = DriftBottle.objects.filter(
            postcard_pair=PostcardPair.objects.filter(receiver=request.user))
        bottles_accessable = bottles_myaccepted.union(bottles_own)
        serializer = DriftBottleSerializer(bottles_accessable, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        '''
            Throw a bottle into drifting bottle pools
        '''
        # get bottle thrown by myself
        bottles_own = DriftBottle.objects.filter(request_name=request.user)
        # get my bottle which has been dragged
        bottles_accepted = bottles_own.exclude(postcard_pair=None)
        # get my been dragged bottle which has not finished
        bottles_unreceived = bottles_accepted.exclude(
            postcard_pair=PostcardPair.objects.filter(sender=request.user, state=3))
        # exist thrown undragged bottle or unreceived bottle
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
            Drag a bottle from drifting bottle pool
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


class DriftBottlePoolDetail(APIView):

    def _get_bottle(self, bottle_id):
        bottle_sets = DriftBottle.objects.filter(pk=bottle_id)
        if not bottle_sets.exists():
            return None
        else:
            return bottle_sets[0]

    def get(self, request, bottle_id, format=None):
        bottle = self._get_bottle(bottle_id)
        if not bottle: 
            return Response(status=status.HTTP_404_NOT_FOUND)
        if (not bottle.request_name == request.user) and (not bottle.postcard_pair.receiver == request.user):
            return Response(status=status.HTTP_403_FORBIDDEN)
        serializer = DriftBottleSerializer(bottle)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def put(self, request, bottle_id, format=None):
        bottle = self._get_bottle(bottle_id)
        if not bottle:
            return Response(status=status.HTTP_404_NOT_FOUND)
        serializer = DriftBottlePoolBottleStateUpdate(data=request.data)
        if not serializer.is_valid():
            return Response(status=status.HTTP_400_BAD_REQUEST)
        # check bottle
        # if bottle not accepted
        if bottle.postcard_pair == None:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        # bottle state can not go back
        if bottle.postcard_pair.state >= serializer.validated_data['state']:
            return Response(status=status.HTTP_406_NOT_ACCEPTABLE)
        # sender can set state to 'sending'
        if bottle.request_name == request.user and not serializer.validated_data['state'] == 2:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # receiver can set state to 'received'
        if bottle.postcard_pair.receiver == request.user and not serializer.validated_data['state'] == 3:
            return Response(status=status.HTTP_403_FORBIDDEN)
        # set state
        bottle.postcard_pair.state = serializer.validated_data['state']
        if serializer.validated_data['state'] == 2:
            bottle.postcard_pair.send_date = datetime.datetime.now()
        elif serializer.validated_data['state'] == 3:
            bottle.postcard_pair.receive_date = datetime.datetime.now()
        bottle.save()
        bottle.postcard_pair.save()
        return Response(status=status.HTTP_201_CREATED)
