from rest_framework import serializers
from .models import AppPlayer, AppGame, AppPlayerstats, AppShotdata
import collections

# Base serializer for all shot data.
class ShotDataSerializer(serializers.ModelSerializer):
    isMake = serializers.BooleanField(source='is_make')
    locationX = serializers.FloatField(source='location_x')
    locationY = serializers.FloatField(source='location_y')

    class Meta:
        model = AppShotdata
        fields = ('isMake', 'locationX', 'locationY')

# Serializer for PlayerStats, nests related shot data for every shot the player made during the game.
class PlayerStatsSerializer(serializers.ModelSerializer):
    isStarter = serializers.BooleanField(source='is_starter')
    minutes = serializers.IntegerField()
    points = serializers.IntegerField()
    assists = serializers.IntegerField()
    offensiveRebounds = serializers.IntegerField(source='offensive_rebounds')
    defensiveRebounds = serializers.IntegerField(source='defensive_rebounds')
    steals = serializers.IntegerField()
    blocks = serializers.IntegerField()
    turnovers = serializers.IntegerField()
    defensiveFouls = serializers.IntegerField(source='defensive_fouls')
    offensiveFouls = serializers.IntegerField(source='offensive_fouls')
    freeThrowsMade = serializers.IntegerField(source='free_throws_made')
    freeThrowsAttempted = serializers.IntegerField(source='free_throws_attempted')
    twoPointersMade = serializers.IntegerField(source='two_pointers_made')
    twoPointersAttempted = serializers.IntegerField(source='two_pointers_attempted')
    threePointersMade = serializers.IntegerField(source='three_pointers_made')
    threePointersAttempted = serializers.IntegerField(source='three_pointers_attempted')
    shots = ShotDataSerializer(source='appshotdata_set', many=True)
    
    class Meta:
        model = AppPlayerstats
        fields = ('isStarter', 'minutes', 'points', 'assists', 'offensiveRebounds', 'defensiveRebounds', 'steals', 'blocks', 'turnovers',
                  'defensiveFouls', 'offensiveFouls', 'freeThrowsMade', 'freeThrowsAttempted', 'twoPointersMade', 'twoPointersAttempted', 'threePointersMade',
                  'threePointersAttempted', 'shots')

# Serializer for Game, nests related PlayerStats that the player achieved during the game.
class GameSerializer(serializers.ModelSerializer):
    date = serializers.DateField()
    player_stats = PlayerStatsSerializer(source='appplayerstats_set', many=True)

    class Meta:
        model = AppGame
        fields = ('date', 'player_stats')

# Serializer for Player, nests related games that the player participated in.
class PlayerSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    games = serializers.SerializerMethodField()

    class Meta:
        model = AppPlayer
        fields = ('name', 'games')

    def get_games(self, obj):
        player_stats = AppPlayerstats.objects.filter(player_id=obj.id).select_related('game_id')
        games_data = collections.defaultdict(list)
        
        for stat in player_stats:
            game_serializer = GameSerializer(stat.game_id).data
            game_serializer['player_stats'] = PlayerStatsSerializer(stat).data
            games_data[stat.game_id.id].append(game_serializer)
        
        return [game for game in games_data.values()]