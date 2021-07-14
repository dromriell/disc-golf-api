from django import forms
from django.contrib.gis import admin
from django.contrib.gis.db import models
from .models import Game, ScoreCard, HoleScore, Stroke
from .forms import StrokeForm


class StrokeInline(admin.StackedInline):
   model = Stroke
   form = StrokeForm


class HoleScoreAdmin(admin.ModelAdmin):
   inlines = [
      StrokeInline,
   ]


class ScoreCardInline(admin.StackedInline):
   model = ScoreCard


class GameAdmin(admin.ModelAdmin):
   inlines = [
      ScoreCardInline,
   ]


admin.site.register(Game, GameAdmin)
admin.site.register(HoleScore, HoleScoreAdmin)
