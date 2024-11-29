from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
)

from drf_spectacular.utils import extend_schema
from .serializers import LeagueSerializer
from .models import League


@extend_schema(tags=['Ligas'])
class ListLeagueView(ListAPIView, CreateAPIView):
    """
    Obtiene la lista de ligas o crea una nueva liga.
    """
    allowed_methods = ['GET', 'POST']
    serializer_class = LeagueSerializer
    queryset = League.objects.all()
    

@extend_schema(tags=['Ligas'])    
class DetailLeagueView(RetrieveUpdateDestroyAPIView):
    allowed_methods = ['GET', 'PUT', 'DELETE']
    serializer_class = LeagueSerializer
    queryset = League.objects.all()