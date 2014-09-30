import csv
data = csv.DictReader(open('World-z10.tsv'), delimiter="\t")
import fiona
import json
import leveldb

db = leveldb.LevelDB("db/geonames")

for row in data:
  geonameid = str(row['geonameid'])
  try:
    correct_name = db.Get(geonameid)
    if row['name'] != correct_name:
      print "{0} should be {1}".format(row['name'], correct_name)
  except Exception:
    pass

