import numpy as np

def drop_na(df_bikes):
    df_bikes.dropna(subset=['GrandTotal','TotalDateAtTheHour'], inplace=True)
    df_bikes.dropna(subset=['Date', 'Time'], inplace=True)
    return df_bikes

def drop_columns_useless(df_bikes):
    return df_bikes.drop(columns=['Remark', 'Unnamed'])

def drop_columns_date(df_bikes):
    return df_bikes.drop(columns=['Date','Time'])
