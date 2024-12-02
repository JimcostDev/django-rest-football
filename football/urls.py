from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from league.viewsets import LeagueViewSet
from team.viewsets import TeamViewSet

# Crear un router único
router = DefaultRouter()
router.register('leagues', LeagueViewSet)  
router.register('teams', TeamViewSet)      

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('docs.urls')),  # Documentación
    path('api/', include(router.urls)), 
]
