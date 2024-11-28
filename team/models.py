from django.db import models
from league.models import League

class Team(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    league = models.ForeignKey(League, on_delete=models.CASCADE, related_name='teams')

    def __str__(self):
        return self.name
