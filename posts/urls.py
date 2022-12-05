from django.urls import path, include
from rest_framework.routers import DefaultRouter

from posts.views import PostViewSet, LikesAPIView, TagAPIView, CommentAPIView

router = DefaultRouter()

router.register("post", PostViewSet, basename="post"),


urlpatterns = [
    path('', include(router.urls)),
    path('tag/', TagAPIView.as_view(), name="tag"),
    path('like/', LikesAPIView.as_view(), name="like"),
    path('comment/', CommentAPIView.as_view(), name="comment")

]
