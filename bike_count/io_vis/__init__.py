import os

url_db_bera = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H19070220_archive.json"
path_target_txt_bera = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "beracasa.txt")
path_target_json_bera = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "beracasa.json")

url_db_lav = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042632_archive.json"
path_target_txt_lav = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "laverune.txt")
path_target_json_lav = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "laverune.json")

url_db_cell = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042633_archive.json"
path_target_txt_cell = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "celleneuve.txt")
path_target_json_cell = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "celleneuve.json")

url_db_la2 = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042634_archive.json"
path_target_txt_la2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "lattes2.txt")
path_target_json_la2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "lattes2.json")

url_db_la1 = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20042635_archive.json"
path_target_txt_la1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "lattes_1.txt")
path_target_json_la1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "lattes1.json")

url_db_vp = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063161_archive.json"
path_target_txt_vp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "vieille_poste.txt")
path_target_json_vp = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "vieille_poste.json")

url_db_ger = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063162_archive.json"
path_target_txt_ger = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "gerhardt.txt")
path_target_json_ger = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "gerhardt.json")

url_db_alb = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_XTH19101158_archive.json"
path_target_txt_alb = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "albert_1er.txt")
path_target_json_alb = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "albert_1er.json")

url_db_del1 = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063163_archive.json"
path_target_txt_del1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "delmas1.txt")
path_target_json_del1 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "delmas1.json")

url_db_del2 = "https://data.montpellier3m.fr/sites/default/files/ressources/MMM_EcoCompt_X2H20063164_archive.json"
path_target_txt_del2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_txt", "delmas2.txt")
path_target_json_del2 = os.path.join(os.path.dirname(os.path.realpath(__file__)), "../data_vis", "data_json", "delmas2.json")

urldb_tab = [url_db_alb, url_db_bera, url_db_cell, url_db_del1, url_db_del2,
             url_db_ger, url_db_la1, url_db_la2, url_db_lav, url_db_vp]
path_target_txt_tab = [path_target_txt_alb, path_target_txt_bera, 
                       path_target_txt_cell, path_target_txt_del1,
                       path_target_txt_del2, path_target_txt_ger,
                       path_target_txt_la1, path_target_txt_la2,
                       path_target_txt_lav, path_target_txt_vp]
path_target_json_tab = [path_target_json_alb, path_target_json_bera,
                        path_target_json_cell, path_target_json_del1,
                        path_target_json_del2, path_target_json_ger,
                        path_target_json_la1, path_target_json_la2,
                        path_target_json_lav, path_target_json_vp]
