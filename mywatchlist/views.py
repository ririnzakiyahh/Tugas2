from django.shortcuts import render
from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers

# Create your views here.
def show_mywatchlist(request):
    watchlist = MyWatchlistItem.objects.all()
    context = {
    'list_movie': watchlist,
    'nama': 'Nisrina Zakiyah Aeni',
    'npm' : '2106635013',
    'pesan' : ""
    }
    film_watched = 0
    film_unwatched = 0
    for films in watchlist :
        if (films.watched_movie == "Sudah") :
            film_watched += 1
        else :
            film_unwatched += 1
    
    if (film_watched >= film_unwatched) :
        context['pesan'] = "Selamat, kamu sudah banyak menonton!"
    else :
        context['pesan'] = "Wah, kamu masih sedikit menonton!"

    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def show_json_by_id(request, id):
    data = MyWatchlistItem.objects.filter(pk=id)
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


