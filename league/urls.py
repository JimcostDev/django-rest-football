from django.urls import path

from .views import (
    ListLeagueView,
    DetailLeagueView,
)

urlpatterns = [
    path('leagues/', ListLeagueView.as_view()),
    path('leagues/<int:pk>/', DetailLeagueView.as_view()),
]