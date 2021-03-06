import pandas as pd


def format_date(df_bikes):
    time_formated = pd.to_datetime(df_bikes['Date'] + " " + df_bikes["Time"], format='%d/%m/%Y %H:%M:%S')
    df_bikes.insert(0, "Date_formated", time_formated)
    df_bikes = df_bikes.set_index('Date_formated').sort_index(ascending=True)
    return df_bikes


def format_date_all(df_dic, date_begin_max):
    date = pd.date_range(start='2021-01-06', end=str(pd.to_datetime('today').normalize()))
    for key in df_dic:
        df_dic[key] = df_dic[key][df_dic[key].index >= date_begin_max]
        for i in range(len(df_dic[key])):
            median = df_dic[key].median()
            if (str(date[i]) != df_dic[key].index[i][0:10] + " " + df_dic[key].index[0][11:19]):
                df_dic[key].loc[str(date[i]).replace(' ', 'T')+'/'+str(date[i+1]).replace(' ', 'T')] = median
                df_dic[key] = df_dic[key].sort_index(ascending=True)
        df_dic[key]['name'] = key
    return(df_dic)


def date_format_simple(df_bikes):
    for i in range(len(df_bikes.index)):
        df_bikes['date'][i] = str(df_bikes.index[i])[0:10]
    return df_bikes
