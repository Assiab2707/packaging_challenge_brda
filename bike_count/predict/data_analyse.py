import pandas as pd
from statistics import mean, median, quantiles
import datetime


def summary_day(df_bikes):
    day = ['Lundi', 'Mardi', 'Mercredi', 'Jeudi',
           'Vendredi', 'Samedi', 'Dimanche']
    summary = pd.DataFrame(columns=['day', 'mean', 'median', 'min', 'max',
                                    'first_quantile', 'third_quantile'])
    for i in range(len(day)):
        sub_df = df_bikes[df_bikes.index.dayofweek == i]['TotalDateSinceMidnight']
        summary.loc[i] = [day[i], mean(sub_df), median(sub_df), min(sub_df),
                          max(sub_df), quantiles(sub_df, n=4)[0],
                          quantiles(sub_df, n=4)[2]]
    return summary


def median_interval(df_bikes):
    data_tmp = pd.DataFrame(columns=['date', 'median'])
    data_tmp['date'] = pd.date_range(start='2020-03-12 09:00:00',
                                     end=str(pd.to_datetime('today').normalize()), 
                                     freq='W-FRI')

    tmp1 = df_bikes[df_bikes.index >= datetime.datetime(2020, 7, 1, 9, 0, 0)]
    tmp1 = tmp1[tmp1.index < datetime.datetime(2020, 9, 1, 9, 0, 0)]
    tmp2 = df_bikes[df_bikes.index >= datetime.datetime(2020, 9, 1, 9, 0, 0)]
    tmp2 = tmp2[tmp2.index < datetime.datetime(2021, 1, 1, 9, 0, 0)]
    tmp3 = df_bikes[df_bikes.index >= datetime.datetime(2021, 1, 1, 9, 0, 0)]
    tmp3 = tmp3[tmp3.index < pd.to_datetime('today').normalize()]

    for i in range(len(data_tmp.index)):
        if (data_tmp['date'][i] < datetime.datetime(2020, 7, 1, 9, 0, 0)):
            data_tmp['median'][i] = median(df_bikes['TotalDateSinceMidnight'][df_bikes.index.date < datetime.date(2020, 7, 1)])
        elif (data_tmp['date'][i] < datetime.datetime(2020, 9, 1, 9, 0, 0)):
            data_tmp['median'][i] = median(tmp1['TotalDateSinceMidnight'])
        elif (data_tmp['date'][i] < datetime.datetime(2020, 12, 15, 9, 0, 0)):
            data_tmp['median'][i] = median(tmp2['TotalDateSinceMidnight'])
        elif (data_tmp['date'][i] < pd.to_datetime('today').normalize()):
            data_tmp['median'][i] = median(tmp3['TotalDateSinceMidnight'])

    for i in range(len(data_tmp.index)):
        if (str(df_bikes.index[i])[0:10] != str(data_tmp.date[i])[0:10]):
            df_bikes.loc[data_tmp.date[i]] = data_tmp['median'][i]
            df_bikes = df_bikes.sort_index(ascending=True)
    return df_bikes
