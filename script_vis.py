import bike_count as bc
import numpy as np
import pandas as pd
import datetime
import matplotlib
from datetimerange import DateTimeRange


df_dic = bc.Load_db_v().save_as_df_tab()
df_coor = pd.DataFrame(columns=['nom','coordonnées'])

date_begin_max = "0000/01/01"
i=0
for key in df_dic: 
    df_coor.loc[i] = [key,df_dic[key]['location'][0]['coordinates']]
    df_dic[key] = bc.drop_columns_useless(df_dic[key], ['laneId', 'location', 'id', 'type','vehicleType', 'reversedLane']).drop_duplicates("dateObserved").set_index(["dateObserved"]).sort_index(ascending=True)
    date_begin_max = max(date_begin_max,df_dic[key].index[0])
    i=i+1
df_dic = bc.format_date_all(df_dic,date_begin_max)

# bc.map_create(df_dic, df_coor)









