from django.shortcuts import render
from musickg.models import Song



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

def aart(request):
    return render(request, 'aart.html', {})

def bart(request):
    return render(request, 'bart.html', {})

def cart(request):
    return render(request, 'cart.html', {})

def dart(request):
    return render(request, 'dart.html', {})

def eart(request):
    return render(request, 'eart.html', {})

def fart(request):
    return render(request, 'fart.html', {})

def gart(request):
    return render(request, 'gart.html', {})

def hart(request):
    return render(request, 'hart.html', {})

def iart(request):
    return render(request, 'iart.html', {})

def jart(request):
    return render(request, 'jart.html', {})

def kart(request):
    return render(request, 'kart.html', {})

def lart(request):
    return render(request, 'lart.html', {})

def mart(request):
    return render(request, 'mart.html', {})

def nart(request):
    return render(request, 'nart.html', {})

def oart(request):
    return render(request, 'oart.html', {})

def part(request):
    return render(request, 'part.html', {})

def qart(request):
    return render(request, 'qart.html', {})

def rart(request):
    return render(request, 'rart.html', {})

def sart(request):
    return render(request, 'sart.html', {})

def tart(request):
    return render(request, 'tart.html', {})

def uart(request):
    return render(request, 'uart.html', {})

def vart(request):
    return render(request, 'vart.html', {})

def wart(request):
    return render(request, 'wart.html', {})

def xart(request):
    return render(request, 'xart.html', {})

def yart(request):
    return render(request, 'yart.html', {})

def zart(request):
    return render(request, 'zart.html', {})
