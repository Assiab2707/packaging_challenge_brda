import datetime


def total_days(df_bikes):
    k = 0
    df_bikes.insert(2, 'TotalDays', 0)
    for i in range(1, len(df_bikes)-1):
        if(i == 1):
            df_bikes.at[df_bikes.index[i-1], "TotalDays"] = df_bikes.at[df_bikes.index[i], "CumulateTotal"] - df_bikes.at[df_bikes.index[i], "TotalDateSinceMidnight"]
        elif(df_bikes.index[i] == datetime.date(2021, 1, 1)):
            df_bikes.at[df_bikes.index[i], "TotalDays"] = df_bikes.at[df_bikes.index[i+1], "CumulateTotal"] - df_bikes.at[df_bikes.index[i+1], "TotalDateSinceMidnight"]
        elif (df_bikes.index[i] < datetime.date(2020, 12, 31)):
            df_bikes.at[df_bikes.index[i-1], "TotalDays"] = df_bikes.at[df_bikes.index[i], "CumulateTotal"] - df_bikes.at[df_bikes.index[i], "TotalDateSinceMidnight"] - df_bikes['TotalDays'].sum()
        elif (df_bikes.index[i] == datetime.date(2020, 12, 31)):
            df_bikes.at[df_bikes.index[i], "TotalDays"] = 566
            df_bikes.at[df_bikes.index[i-1], "TotalDays"] = df_bikes.at[df_bikes.index[i], "CumulateTotal"] - df_bikes.at[df_bikes.index[i], "TotalDateSinceMidnight"]-df_bikes['TotalDays'][0:i-1].sum()
            k = i
        elif (df_bikes.index[i] > datetime.date(2021, 1, 1)):
            df_bikes.at[df_bikes.index[i], "TotalDays"] = df_bikes.at[df_bikes.index[i+1], "CumulateTotal"] - df_bikes.at[df_bikes.index[i+1], "TotalDateSinceMidnight"]-df_bikes['TotalDays'][k+1:].sum()
    return df_bikes


def subdf_byweekday(df_bikes, val):
    df_val = df_bikes[df_bikes.index.dayofweek == val]
    return df_val


def subdf_withoutweekend(df_bikes):
    df_bikes = df_bikes[df_bikes.index.dayofweek != 5]
    df_bikes = df_bikes[df_bikes.index.dayofweek != 6]
    return df_bikes
