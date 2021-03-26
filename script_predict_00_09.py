import bike_count as bc
import numpy as np
import pandas as pd



df = bc.Load_db_p().save_as_df()

df_formated = bc.name_format(df,['Date','Time','CumulateTotal','TotalDateSinceMidnight', 'Unnamed','Remark'])
df_formated = bc.drop_columns_useless(df_formated,['Remark', 'Unnamed','CumulateTotal'])
df_formated = bc.drop_na(df_formated)
df_formated = bc.format_date(df_formated)

df_09 = bc.drop_line_0_9(df_formated)
df_formated = bc.drop_columns_useless(df_formated,['Date','Time'])
df_09 = bc.drop_duplicates_max(df_09)
df_09 = bc.drop_columns_useless(df_09,['Date','Time'])

# bc.histogram_plot(df_09,"Représentation graphique des vélos entre 00h et 09h", "TotalDateSinceMidnight", 675)

df_09_without_we = bc.subdf_withoutweekend(df_09)
# bc.histogram_plot(df_09_without_we,"Représentation graphique des vélos du lundi au vendredi entre 00h et 09h", "TotalDateSinceMidnight", 675)
bc.summary_day(df_09)
print (df_09)