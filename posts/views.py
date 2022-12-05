from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Post, PostLikes, Tag, Comment
from .serializers import PostSerializer, LikesSerializer, TagSerializer, CommentSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author", "date"]

    def get_queryset(self):
        return self.queryset.order_by("date")

    def get_serializer_context(self):
        return {"user": self.request.user}


class LikesAPIView(generics.CreateAPIView):
    queryset = PostLikes.objects.all()
    serializer_class = LikesSerializer

    def perform_create(self, serializer) -> None:
        user = self.request.user
        serializer.save(user=user)


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

