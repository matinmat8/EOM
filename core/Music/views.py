from django.shortcuts import render
from django.http import JsonResponse
from .tasks import increment_post_view_count
from django.views.generic import DetailView
from .models import Music


def detail_getter(request, id):
    music = Music.objects.get(ID=id)
    result = increment_post_view_count.delay(music_id=id)
    return JsonResponse({'task_id': result.task_id})