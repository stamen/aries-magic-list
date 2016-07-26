aries-magic-list
================

What the heck is this?
---
This is an old list of city labels used by many [Stamen](http://stamen.com)-designed basemaps. This list was once used as the input to [Dymo](https://github.com/migurski/dymo), which is a placement script for map labeling, using simulated annealing. We don't use Dymo anymore, but we keep this file around for low-zoom labeling.

Mostly the data appears to come from [Geonames](http://geonames.org), with a significant amount of modification and hand-curation by previous Stamen employees and collaborators. Much of its origins have now been lost to the mists of time.

Who uses it?
---
Currently, this file is used by Stamen's [Toner](https://github.com/stamen/toner-carto) and [Terrain](https://github.com/stamen/terrain-classic) styles, and CARTO's [Positron and Dark Matter](https://github.com/CartoDB/CartoDB-basemaps) styles. Those styles should import the z4to10.json file from http://stamen.github.io/aries-magic-list/z4to10.json at setup time, and should update that file anytime we make data fixes in this repo.

What's up with the name?
---
We call it "magic" because we're not exactly sure how it was originally generated. We could probably find out, we just haven't tried to dig that deep.

We call it "aries" because a long time ago this dataset included a misspelling of Buenos Aires. Long-live the lost city of Buenos Aries!
