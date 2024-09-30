from django.test import TestCase
from rest_framework.test import APIClient
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

class TestRegisterView(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_register_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(Token.objects.count(), 1)

    def test_register_user_with_invalid_data(self):
        data = {
            'username': 'testuser',
        }
        response = self.client.post('/api/register/', data, format='json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(User.objects.count(), 0)
        self.assertEqual(Token.objects.count(), 0)

class TestLoginView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_login_user(self):
        data = {
            'username': 'testuser',
            'password': 'testpassword'
        }
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['token'], str(self.token))

    def test_login_user_with_invalid_data(self):
        data = {
            'username': 'testuser',
        }
        response = self.client.post('/api/login/', data, format='json')
        self.assertEqual(response.status_code, 400)

class TestLogoutView(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user('testuser', 'testuser@example.com', 'testpassword')
        self.token = Token.objects.create(user=self.user)

    def test_logout_user(self):        
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + str(self.token))
        response = self.client.post('/api/logout/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(Token.objects.count(), 0)

    def test_logout_user_without_token(self):
        response = self.client.post('/api/logout/')
        self.assertEqual(response.status_code, 401)