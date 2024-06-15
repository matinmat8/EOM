from django.contrib import admin
from .models import *


class MusicAdminPanel(admin.ModelAdmin):
    prepopulated_fields = {'slug': ['music_name', 'release_date', 'user']}


admin.site.register(Genre)
admin.site.register(Singer)
admin.site.register(Album)
admin.site.register(IntermediateModel)
admin.site.register(Music, MusicAdminPanel)
