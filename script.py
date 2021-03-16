import bike_count

df = bike_count.Load_db().save_as_df()
df_nicely_formated = bike_count.format(df)