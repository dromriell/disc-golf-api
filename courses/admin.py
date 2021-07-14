from django import forms
from django.contrib.gis import admin
from django.contrib.gis.db import models
from .models import Course, Hole
from .forms import CoordinatesWidget, HoleForm

class HoleInline(admin.StackedInline):
   model = Hole
   form = HoleForm
   # formfield_overrides = {
   #    models.PointField: {'widget': CoordinatesWidget}
   # }

class CourseAdmin(admin.ModelAdmin):
   inlines = [
      HoleInline,
   ]

class HoleAdmin(admin.ModelAdmin):
   form = HoleForm


admin.site.register(Course, CourseAdmin)
admin.site.register(Hole, HoleAdmin)