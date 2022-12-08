from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import (
    PostAPIView,
    LikesAPIView,
    TagAPIView,
    CommentAPIView,
    PostLikeAPIView,
    UserPostViewSet
)

router = DefaultRouter()

router.register("user-post", UserPostViewSet, basename="post"),


urlpatterns = [
    path('tag/', TagAPIView.as_view(), name="tag"),
    path('like/', LikesAPIView.as_view(), name="like"),
    path('post/', PostAPIView.as_view()),
    path('post-like/', PostLikeAPIView.as_view(), name="post_like"),
    path('comment/', CommentAPIView.as_view(), name="comment")

]
urlpatterns += router.urls
