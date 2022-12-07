import django_filters

from posts.models import Post


class PostFilterSet(django_filters.FilterSet):
    tag = django_filters.CharFilter(field_name='tag', lookup_expr='name')
    like = django_filters.BooleanFilter(method="get_like_post")

    def get_like_post(self, queryset, name, value):
        if value is True:
            like_post = Post.objects.filter

    class Meta:
        model = Post
        fields = ("tag",)
