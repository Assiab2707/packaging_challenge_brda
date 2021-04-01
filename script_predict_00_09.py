import bike_count as bc


#https://towardsdatascience.com/machine-learning-polynomial-regression-with-python-5328e4e8a386

df = bc.Load_db_p().save_as_df()

df_formated = bc.name_format(df, ['Date', 'Time', 'CumulateTotal',
                                  'TotalDateSinceMidnight', 'Unnamed',
                                  'Remark'])
df_formated = bc.drop_columns_useless(df_formated, ['Remark', 'Unnamed', 'CumulateTotal'])
df_formated = bc.drop_na(df_formated)
df_formated = bc.format_date(df_formated)

df_09 = bc.drop_line_0_9(df_formated)
df_formated = bc.drop_columns_useless(df_formated, ['Date', 'Time'])
df_09 = bc.drop_duplicates_max(df_09)
df_09 = bc.drop_columns_useless(df_09, ['Date', 'Time'])

summary = bc.summary_day(df_09)
print(summary)
bc.histogram_plot(df_09, "Représentation graphique des vélos entre 00h et 09h",
                  "TotalDateSinceMidnight", 675)

df_09_without_we = bc.subdf_withoutweekend(df_09)
bc.histogram_plot(df_09_without_we, "Représentation graphique des vélos du \
                  lundi au vendredi entre 00h et 09h", "TotalDateSinceMidnight",
                  675)

df_09_mon = bc.subdf_byweekday(df_09, 0)
df_09_tues = bc.subdf_byweekday(df_09, 1)
df_09_wed = bc.subdf_byweekday(df_09, 2)
df_09_thur = bc.subdf_byweekday(df_09, 3)
df_09_fri = bc.subdf_byweekday(df_09, 4)
df_09_sa = bc.subdf_byweekday(df_09, 5)
df_09_sun = bc.subdf_byweekday(df_09, 6)
bc.sub_plot_days(df_09_mon, df_09_tues, df_09_wed, df_09_thur, df_09_fri,
                 df_09_sa, df_09_sun, "TotalDateSinceMidnight", 600)

data_regression = bc.median_interval(df_09_fri.sort_index())
bc.non_linear_regression(data_regression)
