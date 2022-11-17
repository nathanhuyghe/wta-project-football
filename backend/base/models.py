from django.db import models


class League(models.Model):
    name = models.CharField(max_length=100)
    logo = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Team(models.Model):
    name = models.CharField(max_length=100)
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    icon = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Standings(models.Model):
    league = models.ForeignKey(League, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    points = models.IntegerField()
    form = models.CharField(max_length=100)
    rank = models.IntegerField()
    played = models.IntegerField()
    win = models.IntegerField()
    draw = models.IntegerField()
    loss = models.IntegerField()


class Player(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    number = models.CharField(max_length=100, null=True)
    position = models.CharField(max_length=100, null=True)
    age = models.CharField(max_length=100)
    birthdate = models.DateField()
    country = models.CharField(max_length=100)
    height = models.IntegerField()
    weight = models.IntegerField()

    def __str__(self):
        return self.lastname


class Fixtures(models.Model):
    id = models.IntegerField(primary_key=True)
    referee = models.CharField(max_length=100, null=True)
    date = models.CharField(max_length=300, null=True)
    venue = models.CharField(max_length=300, null=True)
    status = models.CharField(max_length=300, null=True)
    home_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='home_team')
    away_team = models.ForeignKey(
        Team, on_delete=models.CASCADE, related_name='away_team')
    home_goals = models.IntegerField(null=True)
    away_goals = models.IntegerField(null=True)


class Stats(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    fixture = models.ForeignKey(Fixtures, on_delete=models.CASCADE)
    shots_on_goal = models.IntegerField(null=True)
    shots_off_goal = models.IntegerField(null=True)
    total_shots = models.IntegerField(null=True)
    blocked_shots = models.IntegerField(null=True)
    shots_insidebox = models.IntegerField(null=True)
    shots_outsidebox = models.IntegerField(null=True)
    fouls = models.IntegerField(null=True)
    corner_kicks = models.IntegerField(null=True)
    offsides = models.IntegerField(null=True)
    ball_possesion = models.CharField(max_length=100, null=True)
    yellow_cards = models.IntegerField(null=True)
    red_cards = models.IntegerField(null=True)
    goalkeeper_saves = models.IntegerField(null=True)
    total_passes = models.IntegerField(null=True)
    passes_accurate = models.IntegerField(null=True)


class Lineups(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    formation = models.CharField(max_length=200)
    played = models.IntegerField()
