from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """Manager for user profiles"""

    def createUser(self, email, name, password=None):
        """Create a new user"""
        if not email:
            raise("User must have a email address")

        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        user.set_password(password)
        user.save(using=self.db)

        return user

    def createSuperUser(self, email, name, password):
        """Create a new super user with given details"""
        createUser(email,name,password)

        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)

        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = ['name']

    def get_full_name(self):
        """Retrieve the full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieve the short name of user"""
        return self.name

    def __str__(self):
        """Return string representation of our user"""
        return self.email
