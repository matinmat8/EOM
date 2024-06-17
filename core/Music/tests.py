from django.test import TestCase
from Profile.models import Profile
from django.utils import timezone
from .models import Music, Singer, Genre, Album, IntermediateModel
from django.contrib.auth.models import User


class MusicModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("TestUser", password="12345678")
        genre = Genre.objects.create(genre='Pop')
        singer = Singer.objects.create(name='Drake', genre=genre)
        profile = Profile.objects.create(user=user)
        album = Album.objects.create(album_name='Test Album', genre=genre, release_date=timezone.now(), track_count=10)
        music = Music.objects.create(user=profile, album=album, music_name='Test Music', music_genre=genre, release_date=timezone.now(), pub_date=timezone.now())

        # Create an IntermediateModel instance to link Singer and Music
        IntermediateModel.objects.create(singer=singer, music=music)

    def test_music_query(self):
        # Test querying a Music object
        music = Music.objects.get(music_name='Test Music')
        self.assertEqual(music.music_name, 'Test Music')

        # Test if the singer is assigned correctly
        self.assertTrue(music.singer.filter(name='Drake').exists())
