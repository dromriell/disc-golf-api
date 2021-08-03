import datetime
from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator, URLValidator


def current_year():
      return datetime.date.today().year

def max_year_validator(value):
   return MaxValueValidator(current_year())(value)


class Disc(models.Model):
   DISC_TYPE_CHOICES = [
      ('dist_dr', 'Distance Driver'),
      ('frwy_dr', 'Fairway Driver'),
      ('mid_rng', 'Mid-Range '),
      ('putt', 'Putt/Approach'),
      ('special', 'Specialty'),
   ]
   name = models.CharField(max_length=100)
   manufacturer = models.ForeignKey('Manufacturer', on_delete=models.SET_NULL, null=True, blank=True)
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
   weight = models.FloatField(
      default=0.0,
      blank=True,
      null=True,
      validators=[
         MaxValueValidator(500.0),
         MinValueValidator(0.0)
      ]
   )
   type = models.CharField(choices=DISC_TYPE_CHOICES, max_length=15, default='putt')
   diameter = models.FloatField(default=0.0)
   height = models.FloatField(default=0.0)
   rim_depth = models.FloatField(default=0.0)
   inside_rim_diameter = models.FloatField(default=0.0)
   rim_thickness = models.FloatField(default=0.0)
   rim_depth_to_diameter = models.FloatField(default=0.0)
   rim_configuration = models.FloatField(default=0.0)
   flexibility = models.FloatField(default=0.0)
   disc_class = models.CharField(max_length=50, blank=True, null=True)
   vintage_weight = models.FloatField(blank=True, null=True)
   plastic = models.CharField(max_length=50, blank=True, null=True)
   color = models.CharField(max_length=50, blank=True, null=True)
   img_url = models.URLField(
      validators=[URLValidator],
      blank=True,
      null=True
   )
   img_alt = models.CharField(max_length=40, blank=True, null=True)
   final_year = models.DateField(blank=True, null=True)
   cert_num = models.CharField(max_length=10, blank=True, null=True)
   approval_date = models.DateField(blank=True, null=True)

   def __str__(self):
      return f'{self.manufacturer} {self.name.title()}'


class Manufacturer(models.Model):
   name = models.CharField(max_length=50)
   established = models.IntegerField(
      default=current_year(),
      blank=True,
      null=True,
      validators=[
         max_year_validator,
         MinValueValidator(1900),
      ])
   location = models.CharField(max_length=25, blank=True, null=True)
   is_defunct = models.BooleanField(default=False)

   def __str__(self):
      return f'{self.name.title()}'

   
class UserDisc(models.Model):
   profile = models.ForeignKey('profiles.Profile', on_delete=models.CASCADE, related_name='disc_bag')
   disc = models.ForeignKey(Disc, on_delete=models.SET_DEFAULT, related_name='user_disc', default='DELETED DISC')
   nickname = models.CharField(max_length=50, blank=True, null=True)
   custom_speed = models.IntegerField(
      blank=True,
      null=True,
      validators=[
         MaxValueValidator(14),
         MinValueValidator(1)
      ]
   )
   custom_glide = models.IntegerField(
      blank=True,
      null=True,
      validators=[
         MaxValueValidator(7),
         MinValueValidator(1)
      ]
   )
   custom_turn = models.IntegerField(
      blank=True,
      null=True,
      validators=[
         MaxValueValidator(1),
         MinValueValidator(-5)
      ]
   )
   custom_fade = models.IntegerField(
      blank=True,
      null=True,
      validators=[
         MaxValueValidator(5),
         MinValueValidator(0)
      ]
   )


