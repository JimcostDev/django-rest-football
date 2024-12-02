from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import TeamSerializer
from .models import Team
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

# operaciones crud (create, read, update, delete) para la entidad Team
@extend_schema(tags=['Equipos'])
class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer
    queryset = Team.objects.all()
    permission_classes = [IsAuthenticated]
    
    # Filtrar equipos por liga (liga_id)
    @action(['GET'], detail=False, url_path='filter-by-league/(?P<league_id>[^/.]+)') # expresión regular que define cómo Django debe capturar un parámetro de la URL
    def filter_by_league(self, request, league_id=None):
        """
        Retorna los equipos que pertenecen a una liga específica.
        """
        teams = Team.objects.filter(league_id=league_id)
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)
    