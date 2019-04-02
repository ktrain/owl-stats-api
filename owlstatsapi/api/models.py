import uuid
from django.db import models


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.TextField()
    name = models.TextField()
    abbreviation = models.TextField(unique=True)
    logo_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return "{} {}".format(self.location, self.name)


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField(unique=True)
    role = models.TextField()
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    headshot_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name


class PlayerWeek(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    number = models.PositiveIntegerField()
    player = models.ForeignKey(Player, on_delete=models.PROTECT)
    eliminations = models.PositiveIntegerField()
    deaths = models.PositiveIntegerField()
    healing = models.PositiveIntegerField()
    ultimates = models.PositiveIntegerField()
    final_blows = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return "Week {:d}".format(self.number)
    class Meta:
        verbose_name = 'Player-Week'
