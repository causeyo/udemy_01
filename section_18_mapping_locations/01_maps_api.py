'''As a quick note, you now need to provide a payment card information to use the free google api for maps.
You get $200 of free credit per month, which is much much more than we use for this course.
In case you don't have access to a debit/credit card, an alternative is to use the folium library:

The code for this (assuming you have a  list of latitudes and longitudes) would be:

import folium
hello2 = folium.Map()
fghello = folium.FeatureGroup()
for lat, lon in zip(lats, longs):
      fghello.add_child(folium.CircleMarker(location = [lat,lon], fill = True))
hello2.add_child(fghello)
'''

import csv

lats = []
longs = []

with open('countries.csv') as f:

      file = csv.reader(f)

      for ab,lat,long,name in list(file)[1:]:
            lats.append(float(lat))
            longs.append(float(long))

from bokeh.io import output_file, show

from bokeh.models import GMapPlot, GMapOptions, ColumnarDataSource, Circle, Range1d, PanTool, WheelZoomTool, BoxSelectTool

map_options = GMapOptions(lat=0,lng=0,zoom=3)

plot = GMapPlot(x_range = Range1d(), y_range = Range1d(), map_options=map_options)

plot.title.text = 'Example Plot'

# plot.api_key = input('API KEY:')

source = ColumnarDataSource(data=dict(lat=lats, lon=longs))

circle = Circle(x='lon', y='lat', size=15, fill_color='red', fill_alpha=0.6)

plot.add_glyph(source, circle)
plot.add_tools(PanTool(), WheelZoomTool(), BoxSelectTool())

output_file('my_example_gmap_plot.html')
show(plot)