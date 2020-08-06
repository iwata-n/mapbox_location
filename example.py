from mapbox_location.viz import *
from mapboxgl.utils import df_to_geojson

import pandas as pd

data = pd.DataFrame([
    {'ts': 1, 'azimuth': 90, 'lat':35.6812362, 'lon': 139.7671248},
    {'ts': 2, 'azimuth': 180, 'lat':35.6799683, 'lon': 139.7677253},
    {'ts': 3, 'azimuth': 270, 'lat':35.6699683, 'lon': 139.7677253},
])

properties = ['ts', 'azimuth']
geodata = df_to_geojson(data,
              properties=properties,
              lat='lat', lon='lon', precision=10)

viz = ArrowViz(
    data=geodata,
    center=(35.6812362,139.7671248)
)

viz.export()