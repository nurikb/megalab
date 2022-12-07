from django.urls import path
from rest_framework.routers import DefaultRouter

from posts.views import (
    PostViewSet,
    LikesAPIView,
    TagAPIView,
    CommentAPIView,
    PostLikeViewSet
)

router = DefaultRouter()

router.register("post", PostViewSet, basename="post"),


urlpatterns = [
    path('tag/', TagAPIView.as_view(), name="tag"),
    path('like/', LikesAPIView.as_view(), name="like"),
    path('post-like/', PostLikeViewSet.as_view({'get': 'list'}), name="post_like"),
    path('comment/', CommentAPIView.as_view(), name="comment")

]
urlpatterns += router.urls
