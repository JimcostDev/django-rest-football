from django.urls import path

from .views import (
    ListTeamView,
    DetailTeamView,
    ListTeamByLeagueView,
)

urlpatterns = [
    path('teams/', ListTeamView.as_view()),
    path('teams/<int:pk>/', DetailTeamView.as_view()),
    path('leagues/<int:league_id>/teams/', ListTeamByLeagueView.as_view()),
]