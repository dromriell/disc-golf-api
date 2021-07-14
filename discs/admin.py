from django.contrib import admin
from django.db import models
from .models import Disc, Manufacturer

# Register your models here.
class DiscInline(admin.StackedInline):
   model = Disc


class ManufacturerAdmin(admin.ModelAdmin):
   inlines = [
      DiscInline
   ]


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Disc)

