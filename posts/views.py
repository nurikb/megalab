from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import PostFilterSet
from .models import Post, PostLike, Tag, Comment
from .serializers import PostSerializer, LikePostSerializer, TagSerializer, CommentSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilterSet
    search_fields = ["title", "text"]

    def get_queryset(self):
        if self.action in ("update", "partial_update", "destroy"):
            return self.queryset.filter(author=self.request.user)
        return self.queryset.order_by("-date")

    def get_serializer_context(self):
        return {"user": self.request.user}


class PostLikeViewSet(PostViewSet):
    http_method_names = ["get"]

    def get_queryset(self):
        return self.queryset.filter(post_like__user=self.request.user).order_by("-date")


class LikesAPIView(generics.CreateAPIView):
    queryset = PostLike.objects.all()
    serializer_class = LikePostSerializer

    def perform_create(self, serializer) -> None:
        user = self.request.user
        serializer.save(user=user)


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

