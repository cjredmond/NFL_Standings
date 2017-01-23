from django.db import models

class Team(models.Model):
    city = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()
    ties = models.IntegerField()
    div = models.CharField(max_length=100)

    def __str__(self):
        return self.name
