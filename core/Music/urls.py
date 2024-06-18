from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import detail_getter

app_name = 'music'

urlpatterns = [
    path('detail_getter/<int:id>/', detail_getter),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
