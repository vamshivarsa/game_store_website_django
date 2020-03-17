from django.views import generic
from .models import Game

class IndexView(generic.ListView):
    template_name = 'games/gameindex.html'

    def get_queryset(self):
        return Game.objects.all()


class DetailView(generic.DetailView):
    model = Game
    template_name = 'games/404error.html'