import django_filters

from posts.models import Post


class CharInFilter(django_filters.BaseInFilter, django_filters.CharFilter):
    pass


class PostFilterSet(django_filters.FilterSet):
    tag = CharInFilter(field_name="tag__name", lookup_expr="in")
    author = django_filters.CharFilter(field_name='author__nickname')

    class Meta:
        model = Post
        fields = ("tag", "author")
