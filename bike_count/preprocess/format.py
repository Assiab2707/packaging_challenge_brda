def format(df_bikes):
    df = df_bikes.drop(columns = ['date', 'mois','jour','heure'])
    df.insert(0,"date_formated",df_bikes['date']+"T"+df_bikes['heure']+":00+01:00")
    return df