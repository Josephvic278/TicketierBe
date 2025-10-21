from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model


User = get_user_model()


class AuthTests(APITestCase):
    def test_register_and_token(self):
        url = reverse('auth_register')
        data = {
            'username': 'jane',
            'email': 'jane@example.com',
            'password': 'ComplexPwd123',
            'password2': 'ComplexPwd123'
        }
        resp = self.client.post(url, data, format='json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertTrue(User.objects.filter(username='jane').exists())

        token_url = reverse('token_obtain_pair')
        resp = self.client.post(token_url, {'username': 'jane', 'password': 'ComplexPwd123'}, format='json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertIn('access', resp.data)
