from django.contrib.gis.db import models
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from DG_API.utils.db import parse_pointfield
from courses.models import Course, Hole
from discs.models import Disc

USER = get_user_model()


class Game(models.Model):
   course = models.ForeignKey(Course, on_delete=models.SET_NULL, null=True, blank=False)
   date = models.DateTimeField()
   isInProgress = models.BooleanField(default=True)


class ScoreCard(models.Model):
   player = models.ForeignKey(USER, on_delete=models.SET_NULL, null=True, blank=False)
   game = models.ForeignKey(Game, on_delete=models.SET_NULL, null=True, related_name='scorecards')
   total_score = models.IntegerField(default=0)

   def __str__(self):
      return f'{self.player.username.title()}\'s Scorecard {self.game.date.date()}'


class HoleScore(models.Model):
   score_card = models.ForeignKey(ScoreCard, on_delete=models.CASCADE, related_name='scores')
   hole = models.ForeignKey(Hole, on_delete=models.SET_NULL, null=True, blank=False)
   score = models.IntegerField(default=0)

   def __str__(self):
      return f'{self.score_card} {self.hole} Score'


class Stroke(models.Model):
   id = models.BigAutoField(primary_key=True)
   hole = models.ForeignKey(HoleScore, on_delete=models.CASCADE, related_name='strokes')
   position = models.PointField()
   throw = models.CharField(max_length=30)
   disc = models.ForeignKey(Disc, on_delete=models.SET_NULL, null=True, blank=False)
   dist = models.FloatField()
   isHole = models.BooleanField(default=False)

   def __str__(self):
      return f'{self.hole.hole} {self.dist}ft Throw'

   def parse_coordinates(self, field):
      return parse_pointfield(field)


def players_changed(sender, instance, created, *args, **kwargs):
   if instance.scorecards.count() > 6:
      raise ValidationError('Only six people or less are allowed in one game!')

models.signals.m2m_changed.connect(players_changed, sender=Game.scorecards)
