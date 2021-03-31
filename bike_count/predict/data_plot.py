import seaborn as sns
import statsmodels.formula.api as smf
import pandas as pd
from ipywidgets import interact, IntSlider, FloatLogSlider  # widget manipulation
import subprocess
from IPython.display import HTML
import matplotlib.animation as animation
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

def histogram_plot(df_days, text, col, ylim):
    fig_total = plt.figure(figsize=(25, 5))
    plt.plot(df_days.index,df_days[col])
    plt.title(text)
    plt.ylabel('Nombre de vélos')
    plt.xlabel('Date')
    plt.ylim(0,ylim)
    plt.show()

def sub_plot_days(df_days0,df_days1,df_days2,df_days3,df_days4,df_days5,df_days6, col , ylim):
    fig = plt.figure(figsize=(22, 10))
    plt.suptitle('Représentation du nombre de vélo en fonction du jour de la semaine')
    plt.subplots_adjust(left=0.04, right=0.96, top=0.93, bottom=0.1,hspace=0.4)

    plt.subplot(4, 2, 3,)
    plt.plot(df_days0.index, df_days0[col], 'o-',color='darkblue')
    plt.title('Monday')
    plt.ylim(0,ylim)

    plt.subplot(4, 2, 4)
    plt.title('Tuesday')
    plt.plot(df_days1.index, df_days1[col], 'o-',color='yellow')
    plt.ylim(0,ylim)

    plt.subplot(4, 2, 5)
    plt.title('Wednesday')
    plt.plot(df_days2.index, df_days2[col], 'o-',color='pink')
    plt.ylim(0,ylim)

    plt.subplot(4, 2, 6)
    plt.title('Thursday')
    plt.plot(df_days3.index, df_days3[col], 'o-',color='green')
    plt.ylim(0,ylim)

    plt.subplot(7, 1, 1)
    plt.title('Friday')
    plt.plot(df_days4.index, df_days4[col], 'o-',color='red')
    plt.ylim(0,ylim)

    plt.subplot(4, 2, 7)
    plt.title('Saturday')
    plt.plot(df_days5.index, df_days5[col], 'o-',color='purple')
    plt.ylim(0,ylim)

    plt.subplot(4, 2, 8)
    plt.title('Sunday')
    plt.plot(df_days6.index, df_days6[col], 'o-',color='orange')
    fig.text(0.01, 0.5, 'Nombre de vélos', ha='center', va='center', rotation='vertical')
    plt.ylim(0,ylim)
    plt.show()