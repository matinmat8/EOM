from django.test import TestCase
from Profile.models import Profile
from django.utils import timezone
from .models import Music, Singer, Genre, Album, IntermediateModel
from django.contrib.auth.models import User
from .tasks import increment_post_view_count


class MusicModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user("TestUser", password="12345678")
        genre = Genre.objects.create(genre='Pop')
        singer = Singer.objects.create(name='Drake', genre=genre)
        profile = Profile.objects.create(user=user)
        album = Album.objects.create(album_name='Test Album', genre=genre, release_date=timezone.now(), track_count=10)
        music = Music.objects.create(user=profile, album=album, music_name='Test Music', music_genre=genre, release_date=timezone.now(), pub_date=timezone.now(), views=0)

        # Create an IntermediateModel instance to link Singer and Music
        IntermediateModel.objects.create(singer=singer, music=music)

    def test_music_query(self):
        # Test querying a Music object
        music = Music.objects.get(music_name='Test Music')
        self.assertEqual(music.music_name, 'Test Music')

        # Test if the singer is assigned correctly
        self.assertTrue(music.singer.filter(name='Drake').exists())

    # Testing celery workers
    def test_increment_post_view_count(self):
        music = Music.objects.get(music_name='Test Music')

        increment_post_view_count(music.ID)

        music.refresh_from_db()
        self.assertNotEqual(music.views, 0)

    def test_non_existent_music_query(self):
        with self.assertRaises(Music.DoesNotExist):
            Music.objects.get(music_name='NonExistentMusic')

    def test_empty_music_name_query(self):
        # Query with an empty filter
        empty_query = Music.objects.filter(music_name='')
        self.assertEqual(empty_query.count(), 0)

    def test_invalid_music_query(self):
        with self.assertRaises(Music.DoesNotExist):
            Music.objects.get(music_name=None)

    def test_missing_singer_for_music(self):
        genre = Genre.objects.create(genre='Pop')

        album = Album.objects.create(album_name='Another Album', genre=genre, release_date=timezone.now(),
                                     track_count=8)

        music_without_singer = Music.objects.create(album=album, music_name='No Singer Music', music_genre=genre,
                                                    release_date=timezone.now(), pub_date=timezone.now(), views=0)

        self.assertFalse(music_without_singer.singer.exists())

