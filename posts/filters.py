from django_filters import rest_framework as filters

from posts.models import Post


class PostFilterSet(filters.FilterSet):
    mark = filters.NumberFilter(method="filter_mark")

    def filter_mark(self, queryset, name, value):
        like_posts = Post
        # return queryset.filter(id__in=user_event)

    class Meta:
        model = Post
        fields = ("mark",)
