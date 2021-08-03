from django.contrib import admin
from django.db import models
from django.contrib.admin.views.main import ChangeList
from django.core.paginator import EmptyPage, InvalidPage, Paginator
from .models import Disc, Manufacturer, UserDisc

class InlineChangeList(object):
    can_show_all = True
    multi_page = True
    get_query_string = ChangeList.__dict__['get_query_string']

    def __init__(self, request, page_num, paginator):
        self.show_all = 'all' in request.GET
        self.page_num = page_num
        self.paginator = paginator
        self.result_count = paginator.count
        self.params = dict(request.GET.items())

# Register your models here.
class DiscInline(admin.StackedInline):
   model = Disc
   ordering = ['name']
   per_page = 10
   template = 'stacked_paginated.html'
   extra = 0
   can_delete = False

   def get_formset(self, request, obj=None, **kwargs):
      formset_class = super(DiscInline, self).get_formset(
         request, obj, **kwargs)
      class PaginationFormSet(formset_class):
         def __init__(self, *args, **kwargs):
               super(PaginationFormSet, self).__init__(*args, **kwargs)

               qs = self.queryset
               paginator = Paginator(qs, self.per_page)
               try:
                  page_num = int(request.GET.get('page', ['0'])[0])
               except ValueError:
                  page_num = 0

               try:
                  page = paginator.page(page_num + 1)
               except (EmptyPage, InvalidPage):
                  page = paginator.page(paginator.num_pages)

               self.page = page
               self.cl = InlineChangeList(request, page_num, paginator)
               self.paginator = paginator

               if self.cl.show_all:
                  self._queryset = qs
               else:
                  self._queryset = page.object_list

      PaginationFormSet.per_page = self.per_page
      return PaginationFormSet


class ManufacturerAdmin(admin.ModelAdmin):
   inlines = [
      DiscInline
   ]


admin.site.register(Manufacturer, ManufacturerAdmin)
admin.site.register(Disc)
admin.site.register(UserDisc)

