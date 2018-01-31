from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth import *


class AccountAPITest(APITestCase):

    def _create_user(self):
        # create temp user for testing
        if User.objects.filter(username='pocaetestuser').exists():
            test_user = User.objects.get(username='pocaetestuser')
            test_user.set_password('password')
        else:
            User.objects.create_user(
                'pocaetestuser', 'pocaetestuser@admin.com', 'password')

    def test_account_login(self):
        url = '/api/account/login/'
        data = {'username': 'pocaetestuser', 'password': 'password'}
        self._create_user()
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_account_detail_get(self):
        self._create_user()
        data = {'username': 'pocaetestuser', 'password': 'password'}
        response = self.client.post('/api/account/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.get('/api/account/', format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_account_logout(self):
        self._create_user()
        data = {'username': 'pocaetestuser', 'password': 'password'}
        response = self.client.post('/api/account/login/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        response = self.client.post('/api/account/logout/', format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)