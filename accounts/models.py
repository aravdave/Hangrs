import sys
sys.path.append("..")

from django.db import models
from django.conf import settings
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from datetime import datetime, timedelta
from core.models import TimestampedModel
import jwt


    
class UserManager(BaseUserManager):
    """
    This class inherits basic user functions while providing an implementation for
    create_user and create_superuser
    """
    
    def create_user(self, username, email, password):
        if username is None:
            raise TypeError('Missing username')
        
        if email is None:
            raise TypeError('Missing email address')
        
        if password is None:
            raise TypeError('Missing password')
        
        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()
        
        return user
    
    def create_superuser(self, username, email, password):
        """
        Creates a user with admin permissions
        """
        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        
        return user

class User(AbstractBaseUser, PermissionsMixin, TimestampedModel):

    username = models.CharField(db_index=True, max_length=255, unique=True)

    email = models.EmailField(db_index=True, unique=True)

    is_active = models.BooleanField(default=True)

    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """
        Returns user's email for string representation of user
        """
        return self.email

    @property
    def token(self):
        """
        Allows us to get a user's token by calling `user.token` instead of
        `user.generate_jwt_token().

        The `@property` decorator above makes this possible. `token` is called
        a "dynamic property".
        """
        return self._generate_jwt_token()

    def get_full_name(self):
        """
        Required method that returns the username
        """
        return self.username

    def get_short_name(self):
        """
        Required method that returns the username
        """
        return self.username

    def _generate_jwt_token(self):
        """
        Generates a JSON Web Token that stores this user's ID and has an expiry
        date set to 60 days into the future.
        """
        dt = datetime.now() + timedelta(days=60)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime("%S")),
        }, settings.SECRET_KEY, algorithm='HS256')

        return token
    
    
class Profile(TimestampedModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.URLField(blank=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    date_of_birth = models.DateField(auto_now_add=True)
    confirmed = models.BooleanField(default=False)
    
    def __str__(self):
        return self.user.username