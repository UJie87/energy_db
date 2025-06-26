import pandas as pd
from pyproj import Transformer
import numpy as np
from shapely.geometry import Polygon, mapping
import json

df = pd.read_csv("data/raw/tw_osw_site.csv")


df['site_id']=df['point_code'].str.split('-').str[0].astype(int)

tw97_to_wgs84 = Transformer.from_crs(3826, 4326, always_xy=True)


coords = np.column_stack(tw97_to_wgs84.transform(df['X'].values, df['Y'].values))
df[['lon', 'lat']] = coords

bbox = (
    df.groupby('site_id').agg(min_lon=('lon', 'min'),
                              max_lon=('lon', 'max'),
                              min_lat=('lat', 'min'),
                              max_lat=('lat', 'max'))
                            .reset_index()
)


def make_corners(r):
    return{
        'SW': (r.min_lon, r.min_lat),
        'SW': (r.max_lon, r.min_lat),
        'NE': (r.max_lon, r.max_lat),
        'NW': (r.min_lon, r.max_lat)
    }

bbox['corners']= bbox.apply(make_corners, axis=1)

bbox['geometry']= bbox.apply(
    lambda r: Polygon([
        r.corners['SW'],
        r.corners['SW'],
        r.corners['NE'],
        r.corners['NW']
    ]),
    axis=1
)

geojson = {
    'type': 'FeatureCollection',
    'features':[
        {
            'type': 'Feature',
            'id': int(r.site_id),
            'properties': {'site_id':int(r.site_id)},
            'geometry': mapping(r.geometry)
        }
        for _, r in bbox.iterrows()
    ]
}

with open('osw_bbox.geojson', 'w', encoding='utf-8') as f:
    json.dump(geojson, f, ensure_ascii=False, indent=2)