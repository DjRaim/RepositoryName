from django.urls import path
from musickg.views import index, library, artists, blog

urlpatterns = [
    path('', index, name="index"),
    path('library/', library, name="library" ),
    path('artists/', artists, name="artists" ),
    path('blog/', blog, name="blog"),

    ]
