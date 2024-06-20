from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import DetailGetter

app_name = 'music'

urlpatterns = [
    path('detail_getter/<int:pk>/', DetailGetter.as_view(), name='music_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
