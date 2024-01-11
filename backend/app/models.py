# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AppGame(models.Model):
    date = models.DateField()
    away_team = models.ForeignKey('AppTeam', models.CASCADE)
    home_team = models.ForeignKey('AppTeam',  models.CASCADE, related_name='appgame_home_team_set')

    class Meta:
        db_table = 'games'


class AppPlayer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'players'


class AppPlayerstats(models.Model):
    is_starter = models.BooleanField()
    minutes = models.IntegerField()
    points = models.IntegerField()
    assists = models.IntegerField()
    offensive_rebounds = models.IntegerField()
    defensive_rebounds = models.IntegerField()
    steals = models.IntegerField()
    blocks = models.IntegerField()
    turnovers = models.IntegerField()
    defensive_fouls = models.IntegerField()
    offensive_fouls = models.IntegerField()
    free_throws_made = models.IntegerField()
    free_throws_attempted = models.IntegerField()
    two_pointers_made = models.IntegerField()
    two_pointers_attempted = models.IntegerField()
    three_pointers_made = models.IntegerField()
    three_pointers_attempted = models.IntegerField()
    game_id = models.ForeignKey(AppGame, models.CASCADE, db_column='game_id')
    player_id = models.ForeignKey(AppPlayer, models.CASCADE, db_column='player_id')

    class Meta:
        db_table = 'playerstats'


class AppShotdata(models.Model):
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()
    player_stats = models.ForeignKey(AppPlayerstats,  models.CASCADE)

    class Meta:
        db_table = 'shotdata'


class AppTeam(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'teams'

