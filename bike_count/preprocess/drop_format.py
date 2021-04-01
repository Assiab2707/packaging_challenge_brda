def drop_na(df_bikes):
    df_bikes.dropna(inplace=True)
    return df_bikes


def drop_columns_useless(df_bikes, name_col):
    return df_bikes.drop(columns=name_col)


def drop_line_0_9(df_bikes):
    df_bikes = df_bikes[df_bikes['Time'] <= '09:00:00']
    return df_bikes


def drop_duplicates_max(df_bikes):
    df_bikes = df_bikes.sort_index(ascending=False).drop_duplicates('Date')
    df_bikes = df_bikes.sort_index(ascending=True)
    return df_bikes
