from rest_framework import serializers

from posts.models import Post, Content, User


class ContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Content
        fields = ("type", "value")


class PostSerializer(serializers.ModelSerializer):
    content = ContentSerializer(many=True)

    class Meta:
        model = Post
        fields = ("title", "content")

    def create(self, validated_data):
        content_data = validated_data.pop("content")
        post = Post.objects.create(**validated_data)
        content = [Content(**content, post=post) for content in content_data]
        Content.objects.bulk_create(content)
        return post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'password')
        extra_kwargs = {'password': {'write_only': True}}
