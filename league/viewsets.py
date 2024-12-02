from rest_framework import viewsets
from .serializers import LeagueSerializer
from .models import League
from .permissions import IsBoss
from rest_framework.permissions import IsAuthenticated
from drf_spectacular.utils import extend_schema

# operaciones crud (create, read, update, delete) para la entidad League
@extend_schema(tags=['Ligas'])
class LeagueViewSet(viewsets.ModelViewSet):
    serializer_class = LeagueSerializer
    queryset = League.objects.all()
    permission_classes = [IsAuthenticated, IsBoss]