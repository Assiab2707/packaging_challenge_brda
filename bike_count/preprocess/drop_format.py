import numpy as np

def drop_na(df_bikes):
    df_bikes.dropna(inplace=True)
    return df_bikes

def drop_columns_useless(df_bikes, name_col):
    return df_bikes.drop(columns=name_col)
