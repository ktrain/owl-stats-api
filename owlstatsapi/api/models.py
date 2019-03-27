import uuid
from django.db import models


class Role(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.name.capitalize()


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    location = models.TextField()
    name = models.TextField()
    logo_url = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    @property
    def full_name(self):
        return "{} {}".format(self.location, self.name)


class Player(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.TextField()
    role = models.ForeignKey(Role, on_delete=models.PROTECT)
    team = models.ForeignKey(Team, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
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
    updated_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return "Week {:d}".format(self.number)
