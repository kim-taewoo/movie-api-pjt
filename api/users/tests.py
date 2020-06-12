from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from .models import User
from rest_framework import status
# from pprint import pprint

class ProblemTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        
        self.signup_url = '/rest-auth/registration/'
        self.signin_url = '/rest-auth/login/'
        self.signout_url = '/rest-auth/logout/'

        data = {
            'username': 'testuser1',
            'password': 'testpassword'
        }

        User.objects.create_user(**data)


    def test_signup(self):
        data = {
            'username': 'testuser2',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['user']['username'], data['username'])
        self.assertTrue('token' in response.data)
        self.assertEqual(User.objects.count(), 2)

    
    def test_signup_with_same_username(self):
        data = {
            'username': 'testuser1',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        response = self.client.post(self.signup_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse('token' in response.data)
        self.assertEqual(User.objects.count(), 1)


    def test_signin(self):
        user = User.objects.get(username='testuser1')
        data = {
            'username': 'testuser1',
            'password': 'testpassword',
        }
        response = self.client.post(self.signin_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['user']['username'], data['username'])
        self.assertTrue('token' in response.data)

    
    def test_signout(self):
        user = User.objects.get(username='testuser1')
        data = {
            'username': 'testuser1',
            'password': 'testpassword',
        }
        self.client.post(self.signin_url, data, format='json')
        response = self.client.get(self.signout_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
