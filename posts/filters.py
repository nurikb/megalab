import django_filters

from posts.models import Post


class PostFilterSet(django_filters.FilterSet):
    tag = django_filters.CharFilter(field_name='tag', lookup_expr='name')
    author = django_filters.NumberFilter(field_name='author')

    class Meta:
        model = Post
        fields = ("tag",)
