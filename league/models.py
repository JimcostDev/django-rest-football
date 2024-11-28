from django.db import models

class League(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        # retorna todos los campos de la tabla
        return self.name + ' - ' + self.country
