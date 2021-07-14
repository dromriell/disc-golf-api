import datetime
from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator


class Disc(models.Model):
   name = models.CharField(max_length=30)
   manufacturer = models.OneToOneField('Manufacturer', on_delete=models.SET_NULL, null=True, blank=True)
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
      return f'{self.manufacturer} {self.name.title()}'


def current_year():
      return datetime.date.today().year

def max_year_validator(value):
   return MaxValueValidator(current_year())(value)


class Manufacturer(models.Model):
   name = models.CharField(max_length=50)
   established = models.IntegerField(
      default=current_year(),
      validators=[
         max_year_validator,
         MinValueValidator(1900),
      ])
   location = models.CharField(max_length=25)
   is_defunct = models.BooleanField(default=False)

   def __str__(self):
      return f'{self.name.title()}'

   


