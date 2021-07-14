from copy import error
from django.core import validators
from django.contrib.gis.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from DG_API.utils.db import parse_pointfield

# Create your models here.

class Course(models.Model):
   name = models.CharField(max_length=100)
   city = models.CharField(max_length=100)
   state = models.CharField(max_length=2, null=True, blank=True)
   country = models.CharField(max_length=75)
   zip_code = models.CharField(max_length=15)
   avg_time = models.DecimalField(decimal_places=2, max_digits=4)
   image_url = models.URLField(null=True, blank=True)
   image_alt = models.CharField(max_length=30)

   def __str__(self):
      return self.name.title()

   class Meta:
        ordering = ['name']


class Hole(models.Model):
   course = models.ForeignKey(Course, on_delete=models.CASCADE)
   hole_number = models.IntegerField(
      default=1,
      blank=False,
      null=False,
      validators=[
         MaxValueValidator(50),
         MinValueValidator(1)
      ]
   )
   par = models.IntegerField(
      default=3,
      blank=False,
      null=False,
      validators=[
         MaxValueValidator(10),
         MinValueValidator(1)
      ]
   )
   center = models.PointField()
   tee_box = models.PointField()
   basket = models.PointField()
   avg_score = models.IntegerField(default=0)
   heading = models.IntegerField()

   class Meta:
        constraints = [
            models.UniqueConstraint(fields=['hole_number', 'course'], name='unique_hole_num')
        ]
        ordering = ['hole_number']

   def __str__(self):
      return f'{self.course} - #{self.hole_number}'

   def parse_coordinates(self, field):
      return parse_pointfield(field)

   

   