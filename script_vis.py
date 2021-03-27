import bike_count as bc
import numpy as np
import pandas as pd
import datetime
import matplotlib
from datetimerange import DateTimeRange
import folium
import webbrowser

# https://towardsdatascience.com/visualizing-nyc-bike-data-on-interactive-and-animated-maps-with-folium-plugins-c2d7645cd19b

df_dic = bc.Load_db_v().save_as_df_tab()
date_begin_max = "0000/01/01"
i=0
for key in df_dic: 
    df_dic[key]['name'] = key
    df_dic[key]['long'] = df_dic[key]['location'][0]['coordinates'][0]
    df_dic[key]['lat'] = df_dic[key]['location'][0]['coordinates'][1]
    df_dic[key] = bc.drop_columns_useless(df_dic[key], ['laneId', 'location', 'id', 'type','vehicleType', 'reversedLane']).drop_duplicates("dateObserved").set_index(["dateObserved"]).sort_index(ascending=True)
    date_begin_max = max(date_begin_max,df_dic[key].index[0])
    i=i+1
print(df_dic)
 
df_dic = bc.format_date_all(df_dic,date_begin_max)

df_all = pd.DataFrame(columns=['name','intensity','long','lat','date','color'])

for key in df_dic :
    df_all = df_all.append(df_dic[key])

df_all = df_all.sort_index(ascending=True)
df_all = bc.date_format_simple(df_all)


features = bc.create_geojson_features(df_all)
bc.create_map(features, df_all)
