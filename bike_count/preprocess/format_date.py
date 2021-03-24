import pandas as pd
import numpy as np

def format_date(df_bikes):
    time_formated = pd.to_datetime(df_bikes['Date'] + " "+ df_bikes["Time"], format = '%d/%m/%Y %H:%M:%S')
    df_bikes.insert(0,"Date_formated", time_formated)
    df_bikes = df_bikes.set_index(['Date_formated'])
    df_bikes = df_bikes.sort_index(ascending=True)
    return df_bikes

