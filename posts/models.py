from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)


class Post(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100)
    tag = models.ForeignKey(Tag, max_length=50, null=True, on_delete=models.SET_NULL, related_name="tag")
    date = models.DateField(auto_now_add=True, null=True)


class Content(models.Model):
    type = models.CharField(max_length=10)
    value = models.CharField(max_length=255)
    post = models.ForeignKey(Post, related_name="content", on_delete=models.CASCADE)
