from celery import shared_task
from .models import Music


@shared_task
def increment_post_view_count(music_id):
    music = Music.objects.get(ID=music_id)
    music.views += 1
    music.save()
