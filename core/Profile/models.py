from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    recently_played = models.ManyToManyField('Music.Music', "musics", blank=True, null=True)
    favorite_list = models.ManyToManyField('Music.Music', "favorite_musics", blank=True, null=True)
    introduction = models.TextField(blank=True, null=True)
    # Other profile stuffs will come here....

    def __str__(self):
        return self.user.username


