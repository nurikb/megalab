from django.contrib import admin
from .models import Post, Tag, PostLike, Comment


# Register your models here.
admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(PostLike)
admin.site.register(Comment)
