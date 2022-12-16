import os
from django.conf import settings
from django.test import TestCase
from django.contrib.auth.password_validation import validate_password

class TryDjangoConfigTest(TestCase):
  def test_mytest(self):
    # self.assertNotEqual(2,5)

    # settings.DJANGO_SECRET_KEY
    SECRET_KEY = os.environ.get('SECRET_KEY')
    # self.assertNotEqual(SECRET_KEY,'abc123')
    is_strong = validate_password(SECRET_KEY)