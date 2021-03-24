import pandas as pd
from bike_count.io_vis import urldb_tab, path_target_txt_tab, path_target_json_tab
import os
from tempfile import mkstemp
from shutil import move
import json
from download import download


class Load_db:
  def __init__(self, url=urldb_tab, target_name_txt=path_target_txt_tab, target_name_json=path_target_json_tab):

    for i in range(len(path_target_txt_tab)):
      download(url[i], target_name_txt[i], replace=False)
      format_txt(path_target_txt_tab[i], path_target_json_tab[i])
  
  @staticmethod
  def save_as_df():
    l= []
    for i in range(len(path_target_json_tab)):
      l.insert(i, pd.read_json(path_target_json_tab[i], lines=True))
    return l

def format_txt(path_target_txt, path_target_json):
  fh, abs_path = mkstemp()
  new_file = open(abs_path,'w')
  old_file = open(path_target_txt) 
  for line in old_file:
    new_file.write(line.replace('}{', "}\n{"))
  new_file.close() 
  os.close(fh) 
  old_file.close() 
  move(abs_path,path_target_json)

