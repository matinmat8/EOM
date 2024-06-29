# from django.urls import path
from rest_framework import routers
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register(r'Musics', views.MusicViewSet),

urlpatterns = router.urls
