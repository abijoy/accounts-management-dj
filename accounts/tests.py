from django.test import TestCase
from django.contrib.auth import get_user_model


class AccountsManagersTests(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='general@user.com', password='bar')
        
        self.assertEqual(user.email, 'general@user.com')
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_staff)

        # username is None as you have used AbstractUser
        # it should give Attribute Error if we use AbstractBaseUser
        # then you need to use try-except to handle this case
        self.assertIsNone(user.username)

        with self.assertRaises(TypeError):
            User.objects.create_user()
        with self.assertRaises(TypeError):
            User.objects.create_user(email='')
        with self.assertRaises(ValueError):
            User.objects.create_user(email='', password='foo')
    
    def test_create_superuser(self):
        User = get_user_model()
        admin_user = User.objects.create_superuser(email='super@user.com', password='bar')

        self.assertEqual(admin_user.email, 'super@user.com')
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_superuser)
        self.assertTrue(admin_user.is_staff)

        self.assertIsNone(admin_user.username)

        with self.assertRaises(ValueError):
            User.objects.create_superuser(
                email='super@user',
                password = 'bar',
                is_superuser=False,
            )
            






        
