from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator

# Create your models here.
class Disc(models.Model):
   name = models.CharField(max_length=30)
   manufacturer = models.CharField(max_length=40)
   speed = models.IntegerField(
      default=1,
      blank=False,
      null=False,
      validators=[
         MaxValueValidator(14),
         MinValueValidator(1)
      ]
   )
   glide = models.IntegerField(
      default=1,
      blank=False,
      null=False,
      validators=[
         MaxValueValidator(7),
         MinValueValidator(1)
      ]
   )
   turn = models.IntegerField(
      default=0,
      blank=False,
      null=False,
      validators=[
         MaxValueValidator(1),
         MinValueValidator(-5)
      ]
   )
   fade = models.IntegerField(
      default=0,
      blank=False,
      null=False,
      validators=[
         MaxValueValidator(5),
         MinValueValidator(0)
      ]
   )
   weight = models.IntegerField(
      default=0,
      blank=True,
      null=True,
      validators=[
         MaxValueValidator(500),
         MinValueValidator(0)
      ]
   )
   plastic = models.CharField(max_length=20, blank=True, null=True)
   color = models.CharField(max_length=20),
   img_url = models.URLField(
      validators=[URLValidator]
   )
   img_alt = models.CharField(max_length=20)

   def __str__(self):
      return f'{self.manufacturer} {self.name}'