import csv
import datetime
from .models import Disc, Manufacturer


CSV_PATH = 'discs\pdga-approved-disc-golf-discs_2021-08-01T17-10-54.csv'
def try_float(v):
   try:
       return float(v)
   except Exception:
       return 0.0


with open(CSV_PATH, newline='', encoding="utf8") as discfile:
   disc_reader = csv.reader(discfile, delimiter=',', quotechar='"')
   for row in disc_reader:
      if row[0] == 'Manufacturer / Distributor':
         continue
      disc_manufacturer = Manufacturer.objects.get(name=row[0])
      last_year_dt = datetime.datetime.strptime(row[15], '%b %d, %Y')
      Disc.objects.create(
         manufacturer=disc_manufacturer,
         name=row[1],
         weight=try_float(row[2]),
         diameter=try_float(row[3]),
         height=try_float(row[4]),
         rim_depth=try_float(row[5]),
         inside_rim_diameter=try_float(row[6]),
         rim_thickness=try_float(row[7]),
         rim_depth_to_diameter=try_float(row[8]),
         rim_configuration=try_float(row[9]),
         flexibility=try_float(row[10]),
         disc_class=row[11],
         vintage_weight=try_float(row[12]),
         cert_num=row[14],
         approval_date=last_year_dt,
      )

