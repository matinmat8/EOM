from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save
from django.dispatch import receiver

from Music.models import Music


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recently_played = models.ManyToManyField(Music, "musics", blank=True, null=True)
    favorite_list = models.ManyToManyField(Music, "favorite_musics", blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    # Other profile stuffs will come here....

    def __str__(self):
        return self.user.username


