import bike_count as bc
import numpy as np
import pandas as pd
import datetime
import matplotlib


df1 = bc.Load_db_v().save_as_df()
print(df1)