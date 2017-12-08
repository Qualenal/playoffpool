from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Choice(models.Model):
    home_team_covers = models.BooleanField()
    #Relationships
    related_game = models.ManyToManyField('Game')


class Game(models.Model):
    # TODO: Figure out how to make the games appear on the games template
    home_team = models.CharField(max_length=200)
    away_team = models.CharField(max_length=200)
    line = models.FloatField()
    start_time = models.DateTimeField()
    week = models.IntegerField()
    #Relationships
    related_choice = models.ManyToManyField(Choice, null=True, blank=True)

    def __str__(self):
        return self.away_team + ' @ ' + self.home_team


class UserChoice(models.Model):
    confidence_number = models.ForeignKey('ConfidenceNumber', on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Choice, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class ConfidenceNumber(models.Model):
    value = models.IntegerField()
    user = models.ManyToManyField(User)


