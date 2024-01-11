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
    away_team = models.ForeignKey('AppTeam', models.DO_NOTHING)
    home_team = models.ForeignKey('AppTeam', models.DO_NOTHING, related_name='appgame_home_team_set')

    class Meta:
        managed = False
        db_table = 'app_game'


class AppPlayer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_player'


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
    game_id = models.ForeignKey(AppGame, models.DO_NOTHING)
    player_id = models.ForeignKey(AppPlayer, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_playerstats'


class AppShotdata(models.Model):
    is_make = models.BooleanField()
    location_x = models.FloatField()
    location_y = models.FloatField()
    player_stats = models.ForeignKey(AppPlayerstats, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'app_shotdata'


class AppTeam(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'app_team'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Games(models.Model):
    date = models.DateField()
    home_team = models.ForeignKey('Teams', models.DO_NOTHING, blank=True, null=True)
    away_team = models.ForeignKey('Teams', models.DO_NOTHING, related_name='games_away_team_set', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'games'


class Players(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'players'


class Playerstats(models.Model):
    game = models.ForeignKey(Games, models.DO_NOTHING, blank=True, null=True)
    player = models.ForeignKey(Players, models.DO_NOTHING, blank=True, null=True)
    is_starter = models.BooleanField()
    minutes = models.IntegerField(blank=True, null=True)
    points = models.IntegerField(blank=True, null=True)
    assists = models.IntegerField(blank=True, null=True)
    offensive_rebounds = models.IntegerField(blank=True, null=True)
    defensive_rebounds = models.IntegerField(blank=True, null=True)
    steals = models.IntegerField(blank=True, null=True)
    blocks = models.IntegerField(blank=True, null=True)
    turnovers = models.IntegerField(blank=True, null=True)
    defensive_fouls = models.IntegerField(blank=True, null=True)
    offensive_fouls = models.IntegerField(blank=True, null=True)
    free_throws_made = models.IntegerField(blank=True, null=True)
    free_throws_attempted = models.IntegerField(blank=True, null=True)
    two_pointers_made = models.IntegerField(blank=True, null=True)
    two_pointers_attempted = models.IntegerField(blank=True, null=True)
    three_pointers_made = models.IntegerField(blank=True, null=True)
    three_pointers_attempted = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'playerstats'


class Shotdata(models.Model):
    player_stats = models.ForeignKey(Playerstats, models.DO_NOTHING, blank=True, null=True)
    is_make = models.BooleanField()
    location_x = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    location_y = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'shotdata'


class Teams(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'teams'
