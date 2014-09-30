import leveldb
import shutil
import os
import marshal
import csv
import sys

# create a LevelDB database with geoname id, name.

csv.field_size_limit(sys.maxsize)

try:
  shutil.rmtree("db")
except:
  pass
os.mkdir("db")
geonames_db = leveldb.LevelDB('./db/geonames',error_if_exists=True)

geonames = csv.reader(open('allCountries.txt'), delimiter="\t")

for row in geonames:
  geonames_db.Put(str(row[0]), row[1])

