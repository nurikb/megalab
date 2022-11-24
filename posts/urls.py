from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet

router = DefaultRouter()

router.register("post", PostViewSet, basename="post"),


urlpatterns = [
    path('', include(router.urls)),
]
