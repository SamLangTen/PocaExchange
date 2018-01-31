from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User


class AccountAPITest(APITestCase):
    def test_account_login(self):
        url = '/api/account/login/'
        data = {'username': 'pocaetestuser', 'password': 'password'}
        # create temp user for testing
        if User.objects.filter(username='pocaetestuser').exists():
            test_user = User.objects.get(username='pocaetestuser')
            test_user.set_password('password')
        else:
            User.objects.create_user('pocaetestuser', 'pocaetestuser@admin.com', 'password')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
