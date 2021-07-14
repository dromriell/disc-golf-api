from django.contrib.gis import forms
from django.contrib.gis.geos import Point

class CoordinatesWidget(forms.MultiWidget):
   """ Displays latitude and longitude text fields for use with pointfields. """
   def __init__(self, attrs=None):
      widgets = (forms.TextInput(attrs={'placeholder': 'Latitude'}),
                  forms.TextInput(attrs={'placeholder': 'Longitude'}))
      super(CoordinatesWidget, self).__init__(widgets, attrs)

   def decompress(self, value):
      if value:
         # Reverse the value since Point takes longitude value first
         return tuple(reversed(value.coords))
      return (None, None)

   def value_from_datadict(self, data, files, name):
      lat = data[f'{name}_0']
      lng = data[f'{name}_1']

      try:
         point = Point(float(lng), float(lat), srid=4326)
      except ValueError:
         return ''

      return point