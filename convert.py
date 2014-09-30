import csv
data = csv.DictReader(open('World-z10.tsv'), delimiter="\t")
import fiona
import json

d = []

for row in data:
  latitude = float(row['latitude'])
  longitude = float(row['longitude'])
  f = {}
  f['geometry'] = {
      'type': 'Point',
      'coordinates': [longitude,latitude]
  }
  name = unicode(row['name'],'utf-8')
  f['properties'] = {'name':name,'population':int(row['population']),'zoom':int(row['zoom start']),'capital':row['capital']}
  f['type'] = 'Feature'
  d.append(f)

g = {'type':'FeatureCollection','features':d}
with open('z4to10.json', 'w') as f:
  f.write(json.dumps(g))
