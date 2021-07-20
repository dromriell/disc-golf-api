from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from games.models import ScoreCard
from discs.models import Disc

USER = get_user_model()

# Create your models here.
class Profile(models.Model):
   user = models.OneToOneField(USER, on_delete=models.CASCADE)
   location = models.CharField(max_length=200, null=True, blank=True)
   bio = models.TextField(blank=True, null=True)
   friends = models.ManyToManyField(USER, related_name='friends', blank=True)
   disc_bag = models.ManyToManyField(Disc, related_name='disc_bag', blank=True)

   def __str__(self):
      return f'{self.user.username}\'s Profile'

   def get_last_game(self):
      last_game = ScoreCard.objects.filter(player=self.user.id).latest()
      print(last_game)
      return last_game

def user_created(sender, instance, created, *args, **kwargs):
   if created:
      Profile.objects.get_or_create(user=instance)

post_save.connect(user_created, sender=USER)