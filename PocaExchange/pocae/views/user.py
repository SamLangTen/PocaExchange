from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from pocae.models import *
from pocae.serializers import *
import uuid
import hashlib

class UserList(APIView):
    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, format=None):
        serializer = UserCreationSerializer(data=request.data)
        if serializer.is_valid():
            user = User(user_id=uuid.uuid4())
            user.user_name = serializer.validated_data['user_name']
            hashl = hashlib.sha256()
            hashl.update(serializer.validated_data['password'].encode('utf-8'))
            user.password = hashl.hexdigest()
            user.user_group = serializer.validated_data['user_group']
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)