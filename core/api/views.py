from django.contrib.auth.models import Group, User
from Music.models import Music
from rest_framework import permissions, viewsets

from .serializers import MusicSerializer


class MusicViewSet(viewsets.ModelViewSet):
    queryset = Music.objects.all().order_by('music_name')
    serializer_class = MusicSerializer
    permission_classes = [permissions.IsAuthenticated]
