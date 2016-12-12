from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

class Fixture(models.Model):
    game_no = models.IntegerField()
    round_no = models.IntegerField()
    game_code = models.CharField(max_length=10)
    game_day = models.CharField(max_length=10)
    game_date = models.DateField()
    game_time = models.TimeField()
    time_slot = models.CharField(max_length=2)
    game_state = models.CharField(max_length=4)
    hmaw_status = models.CharField(max_length=2)
    home_team = models.CharField(max_length=30)
    ht_code = models.CharField(max_length=4)
    away_team = models.CharField(max_length=30)
    at_code = models.CharField(max_length=4)
    ground_name = models.CharField(max_length=32)
    rg_no = models.IntegerField()
    def __unicode__(self):
        return '%s %s %s %s' % (self.round_no, self.game_no, self.home_team, self.away_team)

class User(models.Model):
    family_username = models.CharField(max_length=30)
    fav_team = models.CharField(max_length=30)
    def __str__(self):
        return self.family_username

#class Round1(models.Model):
#    username = models.CharField(max_length=30)
#    game_no = models.IntegerField()
#    selected_team = models.CharField(max_length=30)

class Selection(models.Model):
    selected_team = models.CharField(max_length=30)
    def __str__(self):
        return self.selected_team
