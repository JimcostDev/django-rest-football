# from rest_framework.generics import (
#     ListAPIView,
#     CreateAPIView,
#     RetrieveUpdateDestroyAPIView,
# )
# from drf_spectacular.utils import extend_schema
# from .serializers import TeamSerializer
# from .models import Team

# @extend_schema(tags=['Equipos'], 
#                description="Obtiene la lista de equipos o crea un nuevo equipo.",)
# class ListTeamView(ListAPIView, CreateAPIView):
#     allowed_methods = ['GET', 'POST']
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()

# @extend_schema(tags=['Equipos'],
#                description="Obtiene, actualiza o elimina un equipo.")        
# class DetailTeamView(RetrieveUpdateDestroyAPIView):
#     allowed_methods = ['GET', 'PUT', 'DELETE']
#     serializer_class = TeamSerializer
#     queryset = Team.objects.all()

# @extend_schema(tags=['Equipos'],
#                description="Obtiene la lista de equipos de una liga.") 
# # filtrar eqipos por liga (liga id) 
# class ListTeamByLeagueView(ListAPIView):
#     allowed_methods = ['GET']
#     serializer_class = TeamSerializer

#     def get_queryset(self):
#         league_id = self.kwargs['league_id']
#         return Team.objects.filter(league_id=league_id) 