from django.db import models

from core.settings import AUTH_USER_MODEL
from users.validators import validate_file_size


class Tag(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(
        AUTH_USER_MODEL,
        related_name="post_user",
        on_delete=models.CASCADE
    )
    tag = models.ForeignKey(
        Tag,
        max_length=50,
        null=True,
        on_delete=models.SET_NULL,
        related_name="tag"
    )
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(
        upload_to="post_image",
        verbose_name="Картина",
        null=True,
        validators=[validate_file_size],
    )
    text = models.TextField()

    class Meta:
        ordering = ["-date"]

    def __str__(self):
        return f"{self.id}"


class PostLike(models.Model):
    user = models.ForeignKey(
        AUTH_USER_MODEL,
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


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comment")
    user = models.ForeignKey(AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_comment")
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True)

    class Meta:
        ordering = ["date"]

    def __str__(self):
        return f"{self.user}"
