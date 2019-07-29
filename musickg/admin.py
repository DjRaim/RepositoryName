from django.contrib import admin

# Register your models here.
from .models import Playlist, Genre, Author, Song

admin.site.register(Playlist)
admin.site.register(Genre)
admin.site.register(Author)
admin.site.register(Song)
