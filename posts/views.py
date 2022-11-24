from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend


from .models import Post
from .serializers import PostSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["author", "date"]

    def get_queryset(self):
        return self.queryset.order_by("date")


