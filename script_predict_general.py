import bike_count as bc
import numpy as np
import pandas as pd


df = bc.Load_db_p().save_as_df()

df_formated = bc.name_format(df,['Date','Time','GrandTotal','TotalDateAtTheHour', 'Unnamed','Remark'])
df_formated = bc.drop_columns_useless(df_formated,['Remark', 'Unnamed'])
df_formated = bc.drop_na(df_formated)
df_formated = bc.format_date(df_formated)

df_days = df_formated.drop_duplicates("Date")
df_formated = bc.drop_columns_useless(df_formated,['Date','Time'])



df_days = bc.drop_columns_useless(df_days,['Date','Time'])
df_days = bc.total_days(df_days)

print(df_days)
bc.histogram_plot(df_days, "Représentation graphique des vélos par jour")
#566 lien
df_days_mon = bc.subdf_byweekday(df_days,0)
df_days_tues = bc.subdf_byweekday(df_days,1)
df_days_wed = bc.subdf_byweekday(df_days,2)
df_days_thur = bc.subdf_byweekday(df_days,3)
df_days_fri = bc.subdf_byweekday(df_days,4)
df_days_sa = bc.subdf_byweekday(df_days,5)
df_days_sun = bc.subdf_byweekday(df_days,6)

bc.sub_plot_days(df_days_mon,df_days_tues,df_days_wed,df_days_thur,df_days_fri,df_days_sa,df_days_sun)

df_days_withoutwe = bc.subdf_withoutweekend(df_days)
bc.histogram_plot(df_days_withoutwe,"Représentation graphique des vélos du lundi au vendredi")
