from django.contrib import admin
from .models import Post, Content, Tag, PostLikes


# Register your models here.
admin.site.register(Post)
admin.site.register(Content)
admin.site.register(Tag)
admin.site.register(PostLikes)
