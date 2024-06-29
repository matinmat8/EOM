from django.contrib.auth.models import User, Group
from rest_framework import serializers
from Music.models import Music


class MusicSerializer(serializers.ModelSerializer):

    class Meta:
        model = Music
        fields = '__all__'

