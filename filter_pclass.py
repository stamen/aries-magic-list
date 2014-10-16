import csv
import sys

csv.field_size_limit(sys.maxsize)

geonames = csv.reader(open('allCountries.txt'), delimiter="\t")
print "\t".join(["geonameid","name","asciiname","latitude","longitude","featurecode","population"])
for row in geonames:
  if row[6] == 'P':
    print "\t".join([row[0],row[1],row[2],row[4],row[5],row[7],row[14]])

