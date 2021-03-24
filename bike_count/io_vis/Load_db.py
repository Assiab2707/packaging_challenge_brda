import pandas as pd
from bike_count.io_vis import url_db, path_target
import wget
import os
import json



class Load_db:
  def __init__(self, url=url_db, target_name=path_target):
    if (os.path.exists(target_name)==False):
      wget.download(url, target_name)
  
  @staticmethod
  def save_as_df():
    format_json(path_target)
    # df_bikes = pd.read_json(path_target)
    return 2
  
def format_json(path_target):
      with open(path_target) as j:
       data=json.load(j)
       print(data)
