import requests
import os
import django

import sys
sys.path.insert(0, '../')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "owlstatsapi.settings")
django.setup()

from owlstatsapi.api.models import Team, Player

res = requests.get('https://api.overwatchleague.com/teams?locale=en_US')

# iterate through and upsert teams
for teamData in res.json()['competitors']:
    teamData = teamData['competitor']
    nameArray = teamData['name'].split(' ')
    location = ' '.join(nameArray[0:-1])
    name = nameArray[-1]
    abbreviation = teamData['abbreviatedName']
    logo_url = teamData['logo']

    try:
        team = Team.objects.get(abbreviation=abbreviation)
        team.name = name
        team.location = location
        print('Updating existing Team:', name)
    except Team.DoesNotExist:
        team = Team(location=location, name=name, abbreviation=abbreviation, logo_url=logo_url)
        print('Creating new Team:', name)

    team.save()

    # upsert players for the team
    for playerData in teamData['players']:
        playerData = playerData['player']
        name = playerData['name']
        role = playerData['attributes']['role']
        headshot_url = playerData['headshot']
        try:
            player = Player.objects.get(name=name)
            player.role = role
            player.headshot_url = headshot_url
            print('Updating existing Player:', name)
        except Player.DoesNotExist:
            player = Player(name=name, role=role, team=team, headshot_url=headshot_url)
            print('Creating new Player:', name)

        player.save()
