from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """
        creating a new user with email is successful
        """
        email = 'test@email.com'
        password = 'Testpass123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_normalize(self):
        """Test that the new email for user is normalize
        """

        email = "test@GmaIl.com"
        user = get_user_model().objects.create_user(
            email=email,
            password='test123'
        )
        self.assertEqual(user.email, email.lower())

    def test_new_use_without_email(self):
        """Test Creating new user without email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_super_user(self):
        """Test create new super User"""
        user = get_user_model().objects.create_superuser(
            email="test@Gmail.com",
            password='TestPass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
