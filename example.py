from mapbox_location.viz import *
from mapboxgl.utils import df_to_geojson

import pandas as pd

data = pd.DataFrame([
    {'ts': 1, 'azimuth': 90, 'lat':35.6812362, 'lon': 139.7671248, 'color': 'red'},
    {'ts': 2, 'azimuth': 180, 'lat':35.6799683, 'lon': 139.7677253, 'color': 'blue'},
    {'ts': 3, 'azimuth': 270, 'lat':35.6699683, 'lon': 139.7677253, 'color': 'green'},
])

properties = ['ts', 'azimuth', 'color']
geodata = df_to_geojson(data,
              properties=properties,
              lat='lat', lon='lon', precision=10)

viz = ArrowViz(
    data=geodata,
    center=(35.6812362,139.7671248)
)

viz.export()

viz_color = ArrowViz(
    data=geodata,
    center=(35.6812362,139.7671248),
    color='marker.properties["color"]'
)

viz_color.export('color.html')