from django.db import models
from Profile.models import Profile
from taggit.managers import TaggableManager


# What do you think that EOM stands for?
# Think clearly, what can it stand for?


# Only super_user can add type of Genres.
class Genre(models.Model):
    genre = models.CharField(max_length=250)
    # Any extra explanation about this genre.
    genre_description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.genre


class Singer(models.Model):
    name = models.CharField(max_length=250)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, blank=True, null=True)
    birth = models.DateField(blank=True, null=True, verbose_name="Birth Date")
    death = models.DateField(blank=True, null=True, verbose_name="Death Date")
    about_singer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Album(models.Model):
    # If an album had more than one singer.
    singer = models.ManyToManyField(Singer, related_name='albums')
    album_name = models.CharField(max_length=500)
    genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()
    track_count = models.IntegerField()

    def __str__(self):
        return self.album_name


class Music(models.Model):
    ID = models.AutoField(primary_key=True)
    user = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    # Protect of deleting music
    album = models.ForeignKey(Album, on_delete=models.SET_NULL, blank=True, null=True)
    singer = models.ManyToManyField(Singer, through='IntermediateModel')
    music_name = models.CharField(max_length=350)
    music_genre = models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True)
    release_date = models.DateField()
    # When the post has published.
    post_date = models.DateField()
    cover_art = models.FileField(upload_to='media/images/cover_art/')
    music = models.FileField(upload_to='media/music/')
    lyrics = models.TextField(blank=True, null=True)
    review = models.TextField(blank=True, null=True)
    slug = models.SlugField(unique=True)
    views = models.PositiveIntegerField(default=0)
    tag = TaggableManager()

    def __str__(self):
        return self.music_name


# Explicit table to make the relation more clear and using CASCADE deleting method.
class IntermediateModel(models.Model):
    singer = models.ForeignKey(Singer, on_delete=models.SET_NULL, related_name="Singers", null=True)
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name="Music")

    class Meta:
        # Ensuring the uniqueness
        unique_together = ('singer', 'music')

    def __str__(self):
        # Handling if the singer get null data bc of deleting.
        try:
            return f"{self.music.music_name}  sang by {self.singer.name} "
        except:
            return f"{self.music.music_name} There is no singer"


class BandOfMusic(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE)
    # singer = models.ForeignKey(Singer, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    position_in_band = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


# Pictures for music to make the post better looking
class Vibe(models.Model):
    music = models.ForeignKey(Music, on_delete=models.CASCADE, related_name='images')
    picture = models.FileField(upload_to='media/images/vibes/')

    def __str__(self):
        return self.picture.url
