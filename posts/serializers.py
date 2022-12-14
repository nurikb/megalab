from rest_framework import serializers

from posts.models import Post, Tag, PostLike, Comment
from users.serializer import UserSerializer


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(), write_only=True)
    parent = serializers.PrimaryKeyRelatedField(
        queryset=Comment.objects.all(),
        required=False,
        write_only=True
    )
    child = serializers.SerializerMethodField()
    user = UserSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ("id", "user", "post", "text", "parent", "child")

    def validate_parent(self, value):
        if value.parent is not None:
            raise serializers.ValidationError(
                "The parent cannot be a child element of the comment"
            )
        return value

    def get_child(self, obj):
        child = Comment.objects.filter(parent=obj)
        return ChildCommentSerializer(instance=child, many=True).data

    def create(self, validated_data):
        user = self.context.get("user")
        post = Comment(**validated_data)
        post.user = user
        post.save()
        return post


class ChildCommentSerializer(CommentSerializer):
    class Meta(CommentSerializer.Meta):
        fields = ("id", "user", "text", "parent")


class PostSerializer(serializers.ModelSerializer):
    tag = serializers.CharField(source="tag.name")
    is_liked = serializers.SerializerMethodField(read_only=True)
    comment = serializers.SerializerMethodField()
    author = serializers.CharField(source="author.nickname", read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "tag",
            "title",
            "text",
            "image",
            "is_liked",
            "comment",
            "short_desc",
            "author"
        )

    def get_is_liked(self, obj):
        user = self.context.get("user")
        return PostLike.objects.filter(user=user, post=obj).exists()

    def get_comment(self, obj):
        comment = Comment.objects.filter(parent=None, post=obj)
        return CommentSerializer(instance=comment, many=True).data

    def create(self, validated_data):
        tag_data = validated_data.pop("tag").get("name")
        user = self.context.get("user")
        tag, _ = Tag.objects.get_or_create(name=tag_data)
        post = Post(**validated_data, tag=tag)
        post.author = user
        post.save()
        return post


class LikePostSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = "__all__"
