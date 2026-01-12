from django.test import TestCase
from django.urls import reverse
from .models import CustomUser

# Create your tests here.

class SignupTestCase(TestCase):
    def test_signup_view(self):
        response = self.client.post(
            reverse('users:signup'),
            data = {
                'first_name':'aziz',
                'username':'aziz',
                'email':'aziz@gmail.com',
                'password1':'chichqoq',
                'password2':'chichqoq'
            }
        )
        user = CustomUser.objects.get(username='aziz')
        self.assertEqual(user.first_name,'aziz')
        self.assertEqual(user.email,'aziz@gmail.com')
        self.assertTrue(user.check_password('chichqoq'))

        response_second = self.client.get('/users/profile/aziz')
        self.assertEqual(response_second.status_code,200)



        # login
        self.client.login(username='admin',password='admin')

        third_response = self.client.post(
            reverse('users:update'),
            data = {
                'username':'admin',
                'first_name':'admin',
                "last_name":'adminov',
                'email':"aziz@gmail.com",
                'phone_number':'123',
                'tg_username':"@aziz",
            }
        )

        user = CustomUser.objects.get(username='admin')
        print(user)
        self.assertEqual(third_response.status_code, 302)
        self.assertEqual(user.phone_number, '123')
        self.assertEqual(user.first_name, 'admin')



