import pandas as pd
from statistics import mean, median, quantiles

def summary_day(df_bikes):
    day = ['Lundi','Mardi','Mercredi', 'Jeudi', 'Vendredi','Samedi', 'Dimanche']
    summary = pd.DataFrame(columns = ['day','mean','median', 'min', 'max','first_quantile', 'third_quantile' ])
    for i in range(len(day)): 
        sub_df = df_bikes[df_bikes.index.dayofweek==i]['TotalDateSinceMidnight']
        summary.loc[i] = [day[i], mean(sub_df), median(sub_df), min(sub_df), max(sub_df),quantiles(sub_df, n=4)[0], quantiles(sub_df, n=4)[2]]
    return summary