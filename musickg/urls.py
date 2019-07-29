from django.urls import path
from musickg.views import index, library, artists, blog, aart, bart, cart, dart, eart, fart, gart, hart, iart, jart, kart, lart, mart, nart, oart, part, qart, rart, sart, tart, uart, vart, wart, xart, yart, zart

urlpatterns = [
    path('', index, name="index"),
    path('library/', library, name="library" ),
    path('artists/', artists, name="artists" ),
    path('blog/', blog, name="blog" ),
    path('aart', aart, name="aart"),
    path('bart', bart, name="bart"),
    path('cart', cart, name="cart"),
    path('dart', dart, name="dart"),
    path('eart', eart, name="eart"),
    path('fart', fart, name="fart"),
    path('gart', gart, name="gart"),
    path('hart', hart, name="hart"),
    path('iart', iart, name="iart"),
    path('jart', jart, name="jart"),
    path('kart', kart, name="kart"),
    path('lart', lart, name="lart"),
    path('mart', mart, name="mart"),
    path('nart', nart, name="nart"),
    path('oart', oart, name="oart"),
    path('part', part, name="part"),
    path('qart', qart, name="qart"),
    path('rart', rart, name="rart"),
    path('sart', sart, name="sart"),
    path('tart', tart, name="tart"),
    path('uart', uart, name="uart"),
    path('vart', vart, name="vart"),
    path('wart', wart, name="wart"),
    path('xart', xart, name="xart"),
    path('yart', yart, name="yart"),
    path('zart', zart, name="zart"),
    ]
