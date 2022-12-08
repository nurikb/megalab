from rest_framework import viewsets, generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from .filters import PostFilterSet
from .models import Post, PostLikes, Tag, Comment
from .serializers import PostSerializer, LikePostSerializer, TagSerializer, CommentSerializer


class TagAPIView(generics.ListAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class PostAPIView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_class = PostFilterSet
    search_fields = ["title", "text"]

    def get_queryset(self):
        return self.queryset.order_by("-date")


class PostLikeAPIView(PostAPIView):

    def get_queryset(self):
        return self.queryset.filter(post_like__user=self.request.user).order_by("-date")


class UserPostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def get_queryset(self):
        return self.queryset.filter(author=self.request.user)

    def get_serializer_context(self):
        return {"user": self.request.user}


class LikesAPIView(generics.CreateAPIView):
    queryset = PostLikes.objects.all()
    serializer_class = LikePostSerializer

    def perform_create(self, serializer) -> None:
        user = self.request.user
        serializer.save(user=user)


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

