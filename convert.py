import csv
data = csv.DictReader(open('World-z10.tsv'), delimiter="\t")
import fiona
import json
import leveldb

d = []

db = leveldb.LevelDB("db/geonames")

for row in data:
  latitude = float(row['latitude'])
  longitude = float(row['longitude'])
  f = {}
  f['geometry'] = {
      'type': 'Point',
      'coordinates': [longitude,latitude]
  }

  geonameid = str(row['geonameid'])
  name = unicode(row['name'],'utf-8')

  try:
    correct_name = unicode(db.Get(geonameid))
    if name != correct_name:
      name = correct_name
  except Exception:
    pass

  f['properties'] = {'name':name,'population':int(row['population']),'zoom':int(row['zoom start']),'capital':row['capital']}
  f['type'] = 'Feature'
  d.append(f)

g = {'type':'FeatureCollection','features':d}
with open('z4to10.json', 'w') as f:
  f.write(json.dumps(g))
