from django.shortcuts import render
from django.http import JsonResponse
from .tasks import increment_post_view_count
from django.views.generic import DetailView
from .models import Music


class DetailGetter(DetailView):
    # url_name = 'music_detail'
    template_name = 'Music/detailpage.html'
    model = Music

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()
        increment_post_view_count.apply_async(args=([post.ID])).get()
        return context


