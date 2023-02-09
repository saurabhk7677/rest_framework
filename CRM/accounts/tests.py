from .models import AccountManager, User
from django.conf import settings

class MyTest(AccountManager):
    def setUp(self):
        self.user = settings.AUTH_USER_MODEL.objects.create('testuser@test.pl', 'testpass')

    def test_user(self):
        self.assertEqual(self.user, 'testuser@test.pl')

class UserTest(User):
    def setUp(self):
        self.user = settings.AUTH_USER_MODEL.objects.create('testuser@test.pl', 'testpass')

    def test_user(self):
        self.assertEqual(self.user, 'testuser@test.pl')

