from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelsTest(TestCase):
    def test_create_user_with_email(self):
        email = "test@gmail.com"
        password = "123456"
        name = "Mohamed"
        user = get_user_model().objects.create_user(
            email=email, password=password, name=name
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_is_normalized(self):
        email = "test@GMAIL.COM"
        user = get_user_model().objects.create_user(email, "test123")
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "test123")

    def test_create_super(self):
        user = get_user_model().objects.create_superuser(
            email='yh10445@gmail.com', password="123456", name="mohamed")

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
