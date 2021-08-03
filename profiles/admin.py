from django.contrib import admin
from .models import Profile
from discs.models import UserDisc

class UserDiscInline(admin.TabularInline):
   model = UserDisc

class ProfileAdmin(admin.ModelAdmin):
   inlines = [
      UserDiscInline
   ]

# Register your models here.
admin.site.register(Profile, ProfileAdmin)