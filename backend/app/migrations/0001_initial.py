# Generated by Django 4.2.4 on 2023-08-28 19:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AppGame',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
            options={
                'db_table': 'games',
            },
        ),
        migrations.CreateModel(
            name='AppPlayer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'players',
            },
        ),
        migrations.CreateModel(
            name='AppPlayerstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_starter', models.BooleanField()),
                ('minutes', models.IntegerField()),
                ('points', models.IntegerField()),
                ('assists', models.IntegerField()),
                ('offensive_rebounds', models.IntegerField()),
                ('defensive_rebounds', models.IntegerField()),
                ('steals', models.IntegerField()),
                ('blocks', models.IntegerField()),
                ('turnovers', models.IntegerField()),
                ('defensive_fouls', models.IntegerField()),
                ('offensive_fouls', models.IntegerField()),
                ('free_throws_made', models.IntegerField()),
                ('free_throws_attempted', models.IntegerField()),
                ('two_pointers_made', models.IntegerField()),
                ('two_pointers_attempted', models.IntegerField()),
                ('three_pointers_made', models.IntegerField()),
                ('three_pointers_attempted', models.IntegerField()),
                ('game_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appgame')),
                ('player_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appplayer')),
            ],
            options={
                'db_table': 'playerstats',
            },
        ),
        migrations.CreateModel(
            name='AppTeam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'teams',
            },
        ),
        migrations.CreateModel(
            name='AppShotdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_make', models.BooleanField()),
                ('location_x', models.FloatField()),
                ('location_y', models.FloatField()),
                ('player_stats', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appplayerstats')),
            ],
            options={
                'db_table': 'shotdata',
            },
        ),
        migrations.AddField(
            model_name='appgame',
            name='away_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.appteam'),
        ),
        migrations.AddField(
            model_name='appgame',
            name='home_team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appgame_home_team_set', to='app.appteam'),
        ),
    ]
