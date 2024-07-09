from django.contrib.auth.models import Group, User
from Music.models import Music
from Music.tasks import increment_post_view_count
from rest_framework import permissions, viewsets
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from .permissions import IsOwnerOrAdmin

from .serializers import MusicSerializer


class MusicViewSet(viewsets.ViewSet):

    def list(self, request, **kwargs):
        queryset = Music.objects.all().order_by('music_name')
        serializer_class = MusicSerializer(queryset, many=True)
        permission_classes = [permissions.IsAuthenticated]
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = Music.objects.all()
        music = get_object_or_404(queryset, pk=pk)
        serializer = MusicSerializer(music)
        increment_post_view_count.apply_async(args=([pk])).get()
        return Response(serializer.data)

