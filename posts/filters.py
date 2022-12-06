import django_filters

from posts.models import Post


class PostFilterSet(django_filters.FilterSet):
    tag = django_filters.CharFilter(field_name='tag', lookup_expr='name')
    date = django_filters.CharFilter(field_name='date')
    author = django_filters.CharFilter(field_name='author', lookup_expr='nickname')

    # def tag_mark(self, queryset, name, value):
    #     tag_post = queryset.objects.filter(tag__name=value)
    #     return tag_post

    class Meta:
        model = Post
        fields = ("tag",)
