import folium
import webbrowser
import branca
from folium.plugins import HeatMapWithTime, TimeSliderChoropleth
from bike_count.vis import path_target
import pandas as pd
from folium.plugins import TimestampedGeoJson
import branca.colormap as cmp

import bike_count as bc
import numpy as np
import matplotlib


def add_color(df_bikes) :
    min_max = [min(df_bikes['intensity']), max(df_bikes['intensity'])]
    cm = branca.colormap.LinearColormap(['yellow', 'darkred'], vmin=min_max[0], vmax=min_max[1])
    for i in range(len(df_bikes['intensity'])):
        df_bikes['color'][i] = cm(df_bikes['intensity'][i])
    return df_bikes


def create_geojson_features(df):
    df = add_color(df)
    features = []
    for _, row in df.iterrows():
        feature = {
            'type': 'Feature',
            'geometry': {
                'type':'Point', 
                'coordinates':[row['long'],row['lat']],
            },
            'properties': {
                'time': row['date'],
                'style': {'color' : ''},
                'icon': 'circle',
                'iconstyle':{
                    'fillColor': row['color'],
                    'fillOpacity': 0.9,
                    'stroke': 'True',
                    'radius': row['intensity'] * 0.025,
                },
                'popup': str(row['name']) + ' : ' + str(int(row['intensity']))
            }
        }
        features.append(feature)
    return features

def create_map(features, df_bikes):   
    map = folium.Map(location=[43.595092,3.871105],zoom_start=12.50 ,min_zoom=11.5, max_zoom =14.5,max_bounds=True)
    TimestampedGeoJson(
        {'type': 'FeatureCollection',
        'features': features}
        , period='P1D'
        , duration = 'PT1M'
        , add_last_point=False
        , transition_time=500
        , auto_play=True
        , max_speed=1
        , loop=True
        , loop_button=True
        , date_options='YYYY-MM-DD'
        , time_slider_drag_update=False
    ).add_to(map)
    color_legend(map,df_bikes)
    map.save(path_target)
    webbrowser.open(path_target)    

def color_legend(map, df_bikes):
    min_max = [min(df_bikes['intensity']), max(df_bikes['intensity'])]
    linear = cmp.LinearColormap(['yellow', 'orange','red', 'darkred'],vmin=min_max[0], vmax=min_max[1], caption='Nombre de vélo')
    linear.add_to(map)

