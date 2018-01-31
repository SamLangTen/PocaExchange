from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import *
from api.models import DriftBottle

class DriftBottleAPITest(APITestCase):

    def _create_user(self):
        # create temp user for testing
        if User.objects.filter(username='pocaetestuser').exists():
            test_user = User.objects.get(username='pocaetestuser')
            test_user.set_password('password')
        else:
            User.objects.create_user(
                'pocaetestuser', 'pocaetestuser@admin.com', 'password')

    def _login(self):
        data = {'username': 'pocaetestuser', 'password': 'password'}
        response = self.client.post('/api/account/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_drift_bottle_throw(self):
        self._create_user()
        self._login()
        response = self.client.post('/api/driftbottle/pools/', format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        response = self.client.post('/api/driftbottle/pools/', format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_drift_bottle_get(self):
        self._create_user()
        self._login()
        response = self.client.get('/api/driftbottle/', format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        user = User.objects.get(username='pocaetestuser')
        #set admin
        user.is_staff = True
        user.save()
        response = self.client.get('/api/driftbottle/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)