from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Content(models.Model):
    type = models.CharField(max_length=10)
    value = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name="content", on_delete=models.CASCADE)
