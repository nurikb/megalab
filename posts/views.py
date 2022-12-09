from rest_framework import viewsets, generics, status
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response

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


class LikesAPIView(APIView):
    queryset = PostLike.objects.all()
    serializer_class = LikePostSerializer

    def get(self, request):
        like_post = Post.objects.filter(post_like__user=self.request.user).order_by("-date")
        serializer = PostSerializer(like_post, many=True, context={"user": request.user})
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        data.update({"user": request.user.id})
        serializer = LikePostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CommentAPIView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_serializer_context(self):
        return {"user": self.request.user}

