from rest_framework import serializers
from webapp.models import Photo, Comment


class CommentSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'image', 'created_at', 'author')


class PhotoSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    photo_comments = CommentSerializer(many=True, read_only=True, source='comments_photo')

    class Meta:
        model = Photo
        fields = ('id', 'image', 'signature', 'created_at', 'like_amount', 'author', 'photo_comments')





