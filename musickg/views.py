from django.shortcuts import render



def index(request):
    songs = Song.objects.all()
    return render(request, 'index.html', {
    'songs':songs
    })

def library(request):
    return render(request, 'library.html', {})

def artists(request):
    return render(request, 'artists.html', {})

def blog(request):
    return render(request, 'blog.html', {})
