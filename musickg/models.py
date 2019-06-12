from django.db import models

class Playlist(models.Model):
    user=models.ForeignKey('user.User', on_delete=models.CASCADE, related_name='playlists')

    title=models.CharField(max_length=30)

    trackscount=models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return self.title

class Genre(models.Model):
    title=models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Author(models.Model):
    name=models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Song(models.Model):
    title=models.CharField(max_length=255)

    year=models.PositiveSmallIntegerField()

    genre=models.ForeignKey(Genre, on_delete=models.SET_NULL, null=True, blank=True)

    author=models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)

    playlist=models.ManyToManyField(Playlist)


    file=models.FileField()

    def __str__(self):
        return self.title








