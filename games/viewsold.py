from django.shortcuts import render

from django.http import HttpResponse,Http404
from .models import Game


def index(request):
    all_games=Game.objects.all()
    return render(request,'games/gameindex.html',
                    {'all_games':all_games})
                    
    #old format withou out render(here we used HttpResponse)
    #-------------------------------------------------------------
    '''html=''
    for game in all_games:
        url ='/games/' + str(game.id) + '/'
        html+= '<a href ="' + url + '">'+str(game.name) + '</a><br>'
    return HttpResponse(html)'''
    #---------------------------------------------------------
    

def details(request,game_id):
    try:
        game=Game.objects.get(id=game_id)
    except Game.DoesNotExist:
        raise Http404("THIS GAME IS NOT EXIST")

    return render(request,'games/404error.html',{'game':game})
