from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from .serializers import TeamSerializer
from .models import Team

class ListTeamView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de equipos o crea un nuevo equipo.
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    
class DetailTeamView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = TeamSerializer
    queryset = Team.objects.all()

# filtrar eqipos por liga (liga id) 
class ListTeamByLeagueView(ListAPIView):
    allowed_methods = ['GET']
    serializer_class = TeamSerializer

    def get_queryset(self):
        league_id = self.kwargs['league_id']
        return Team.objects.filter(league_id=league_id) 