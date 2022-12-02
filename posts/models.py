from django.db import models

from core import settings


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    tag = models.ForeignKey(
        Tag,
        max_length=50,
        null=True,
        on_delete=models.SET_NULL,
        related_name="tag"
    )
    date = models.DateField(auto_now_add=True)
    image = models.ImageField(verbose_name="Картина", null=True)
    text = models.TextField()


class PostLikes(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="user_like",
        on_delete=models.CASCADE
    )
    post = models.ForeignKey(
        Post,
        related_name="post_like",
        on_delete=models.CASCADE
    )

    def __str__(self):
        return f"{self.user}-{self.post}"


class Content(models.Model):
    type = models.CharField(max_length=10)
    value = models.CharField(max_length=255)
    post = models.ForeignKey(
        Post,
        related_name="content",
        on_delete=models.CASCADE
    )
