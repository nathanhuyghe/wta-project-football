from django.contrib import admin

# Register your models here.

from .models import Fixtures, Team, Player, League, Standings, Lineups

admin.site.register(Team)
admin.site.register(Player)
admin.site.register(League)
admin.site.register(Standings)
admin.site.register(Fixtures)
admin.site.register(Lineups)
