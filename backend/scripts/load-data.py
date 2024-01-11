import psycopg2
import json

# Database connection parameters
db_params = {
    "host": "localhost",
    "database": "okc",
    "user": "okcapplicant",
    "password": "thunder"
}

# Load JSON files
with open("./raw_data/players.json") as f:
    players_data = json.load(f)

with open("./raw_data/teams.json") as f:
    teams_data = json.load(f)

with open("./raw_data/games.json") as f:
    games_data = json.load(f)


conn = psycopg2.connect(**db_params)
cursor = conn.cursor()

cursor.execute("SELECT COALESCE(MAX(id), 0) FROM app.players")
playerSerialID = cursor.fetchone()[0] + 1
print(playerSerialID)
# Insert data into Players table
for player in players_data:
    cursor.execute("INSERT INTO app.players (id, name) VALUES (%s, %s)", (playerSerialID, player["name"]))
    playerSerialID += 1

cursor.execute("SELECT COALESCE(MAX(id), 0) FROM app.Teams")
teamSerialID = cursor.fetchone()[0] + 1
# Insert data into Teams table
for team in teams_data:
    cursor.execute("INSERT INTO app.Teams (id, name) VALUES (%s, %s)", (teamSerialID, team["name"]))
    teamSerialID += 1

cursor.execute("SELECT COALESCE(MAX(id), 0) FROM app.PlayerStats")
playerStatsSerialIdCounter = cursor.fetchone()[0] + 1
cursor.execute("SELECT COALESCE(MAX(id), 0) FROM app.Games")
gameSerialID = cursor.fetchone()[0] + 1
# Insert data into Games
for game in games_data:
    cursor.execute("INSERT INTO app.Games (id, date, home_team_id, away_team_id) VALUES (%s, %s, %s, %s)", (gameSerialID, game["date"], game["homeTeam"]["id"], game["awayTeam"]["id"]))
    
    # Insert data into PlayerStats
    # f"isStarter": false, "minutes": 16, "points": 12, "assists": 1, "offensiveRebounds": 0, "defensiveRebounds": 3, "steals": 0, "blocks": 1, "turnovers": 0, "defensiveFouls": 1, "offensiveFouls": 0, "freeThrowsMade": 0, "freeThrowsAttempted": 0, "twoPointersMade": 0, "twoPointersAttempted": 0, "threePointersMade": 4, "threePointersAttempted": 5
    for player in game["homeTeam"]["players"]:
        cursor.execute("INSERT INTO app.PlayerStats (id, game_id, player_id, is_starter, minutes, points, assists, offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls, free_throws_made, free_throws_attempted, two_pointers_made, two_pointers_attempted, three_pointers_made, three_pointers_attempted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (playerStatsSerialIdCounter, game["id"], player["id"], player["isStarter"], player["minutes"], player["points"], player["assists"], player["offensiveRebounds"], player["defensiveRebounds"], player["steals"], player["blocks"], player["turnovers"], player["defensiveFouls"],
                    player["offensiveFouls"], player["freeThrowsMade"], player["freeThrowsAttempted"], player["twoPointersMade"], player["twoPointersAttempted"], player["threePointersMade"], player["threePointersAttempted"]))
        
        # Insert data into ShotData
        # {"isMake": true, "locationX": 0.2, "locationY": 25.1}
        for shot in player["shots"]:
            cursor.execute("INSERT INTO app.ShotData (player_stats_id, is_make, location_x, location_y) VALUES (%s, %s, %s, %s)", 
                           (playerStatsSerialIdCounter, shot["isMake"], shot["locationX"], shot["locationY"]))

        playerStatsSerialIdCounter += 1
        
    # Insert data into PlayerStats    
    for player in game["awayTeam"]["players"]:
        cursor.execute("INSERT INTO app.PlayerStats (id, game_id, player_id, is_starter, minutes, points, assists, offensive_rebounds, defensive_rebounds, steals, blocks, turnovers, defensive_fouls, offensive_fouls, free_throws_made, free_throws_attempted, two_pointers_made, two_pointers_attempted, three_pointers_made, three_pointers_attempted) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (playerStatsSerialIdCounter, game["id"], player["id"], player["isStarter"], player["minutes"], player["points"], player["assists"], player["offensiveRebounds"], player["defensiveRebounds"], player["steals"], player["blocks"], player["turnovers"], player["defensiveFouls"],
                    player["offensiveFouls"], player["freeThrowsMade"], player["freeThrowsAttempted"], player["twoPointersMade"], player["twoPointersAttempted"], player["threePointersMade"], player["threePointersAttempted"]))
        
        # Insert data into ShotData
        for shot in player["shots"]:
            cursor.execute("INSERT INTO app.ShotData (player_stats_id, is_make, location_x, location_y) VALUES (%s, %s, %s, %s)", 
                           (playerStatsSerialIdCounter, shot["isMake"], shot["locationX"], shot["locationY"]))

        playerStatsSerialIdCounter += 1
    
    gameSerialID += 1


conn.commit()
cursor.close()
conn.close()