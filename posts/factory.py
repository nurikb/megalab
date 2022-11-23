from django.contrib.auth.models import User

import factory
from posts.models import Post, Content


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    id = 1
    username = 'user1'
    password = 'user1'


class PostFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Post


class ContentFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Content
