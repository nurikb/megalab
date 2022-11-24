from rest_framework import serializers

from posts.models import Post, Content, Tag


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("type", "value")


class PostSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)
    tag = serializers.CharField(source="tag.name")

    class Meta:
        model = Post
        fields = "__all__"

    def create(self, validated_data):
        content_data = validated_data.pop("content")
        tag_data = validated_data.pop("tag")
        tag, _ = Tag.objects.get_or_create(tag_data)
        post = Post.objects.create(**validated_data, tag=tag)
        content = [Content(**content, post=post) for content in content_data]
        Content.objects.bulk_create(content)

        return post
