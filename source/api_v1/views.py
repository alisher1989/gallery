from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import Photo, Comment
from .serializers import PhotoSerializer, CommentSerializer


class LogoutView(APIView):
    permission_classes = [AllowAny]

    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            user.auth_token.delete()
        return Response({'status': 'OK'})


class PhotoViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = PhotoSerializer
    queryset = Photo.objects.all()

    @action(methods=['post'], detail=True)
    def like_up(self, request, pk=None):
        like = self.get_object()
        like.like_amount += 1
        like.save()
        return Response({'id': like.pk, 'rating': like.like_amount})

    @action(methods=['post'], detail=True)
    def like_down(self, request, pk=None):
        like = self.get_object()
        like.like_amount -= 1
        like.save()
        return Response({'id': like.pk, 'rating': like.like_amount})


class CommentViewSet(viewsets.ModelViewSet):
    permission_classes = [AllowAny]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()

    def get_permissions(self):
        if self.action not in ['update', 'partial_update', 'destroy']:
            return [AllowAny()]
        return [IsAuthenticated()]