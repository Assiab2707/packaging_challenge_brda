import pandas as pd
from statistics import median

def summary_day(df_bikes):
    day = ['Lundi','Mardi','Mercredi', 'Jeudi', 'Vendredi','Samedi', 'Dimanche']
    summary = pd.DataFrame(columns=day)
    for i in range(len(day)): 
        summary[day].append[day[i]]
        summary.append(df_bikes[df_bikes.index.dayofweek==i].describe())
        print (summary)
