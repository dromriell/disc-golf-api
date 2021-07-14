from django.core.exceptions import ValidationError

def parse_pointfield(field):
   """ Takes a pointfield and returns json compatable coordinates """
   try:
      return {
         'lat':field.coords[1],
         'lng':field.coords[0]
      }
   except KeyError:
      raise ValidationError(f'{field} is not a PointField!')