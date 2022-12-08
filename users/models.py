from django.contrib.auth.models import AbstractUser
from django.db import models

from users.managers import CustomUserManager


class User(AbstractUser):
    nickname = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to="user_profile", null=True)

    USERNAME_FIELD = 'nickname'

    username = None

    objects = CustomUserManager()

    def __str__(self):
        return self.nickname
