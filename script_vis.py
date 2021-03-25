import bike_count as bc
import numpy as np
import pandas as pd
import datetime
import matplotlib
from datetimerange import DateTimeRange


df_dic = bc.Load_db_v().save_as_df()
date_begin_max = "0000/01/01"
for key in df_dic: 
    df_dic[key] = bc.drop_columns_useless(df_dic[key], ['laneId', 'location', 'id', 'type','vehicleType', 'reversedLane']).drop_duplicates("dateObserved").set_index(["dateObserved"]).sort_index(ascending=True)
    date_begin_max = max(date_begin_max,df_dic[key].index[0])

df_dic = bc.format_date_all(df_dic,date_begin_max)

print(df_dic)


