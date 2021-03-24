import bike_count as bc
import numpy as np
import pandas as pd
import datetime
import matplotlib


list_df = bc.Load_db_v().save_as_df()

df_alb = bc.drop_columns_useless(list_df[0],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_bera = bc.drop_columns_useless(list_df[1],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_cell = bc.drop_columns_useless(list_df[2],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_del1 = bc.drop_columns_useless(list_df[3],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_del2 = bc.drop_columns_useless(list_df[4],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_ger = bc.drop_columns_useless(list_df[5],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_la1 = bc.drop_columns_useless(list_df[6],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_la2 = bc.drop_columns_useless(list_df[7],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_lav = bc.drop_columns_useless(list_df[8],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])
df_vp = bc.drop_columns_useless(list_df[9],['laneId', 'location', 'id', 'type',
       'vehicleType', 'reversedLane'])


print(len(df_vp))
print(len(df_lav))
print(len(df_la2))
print(len(df_la1))
print(len(df_ger))
print(len(df_alb))
print(len(df_cell))
print(len(df_bera))
print(len(df_del1))
print(len(df_del2))

print(df_bera)


