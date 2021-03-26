import folium
import webbrowser
import branca
from folium.plugins import HeatMapWithTime, TimeSliderChoropleth
import branca.colormap as cmp
from bike_count.vis import path_target


def map_create(df_dic, df_coor):
    map = folium.Map(location=[43.595092,3.871105],zoom_start=12.45 ,min_zoom=11.5, max_zoom =14.5,max_bounds=True)

    title_html = '''
     <head><style> html { overflow-y: hidden; } </style></head>
     <h3 align="center" style="font-size:20px"><b>Représentation du nombre de vélos df_dic['Albert 1er'].index[0] </b></h3>
     ''' 
    map.get_root().html.add_child(folium.Element(title_html))
    circle_marker_day(df_coor, map, df_dic['Albert 1er'].index[0], df_dic)
    # time_bar(map,df_dic)
    color_legend(map)

    # _ = TimeSliderChoropleth(
    #     data=df_dic['Albert 1er'].to_json(),
    #     styledict=style_dict,
    # ).add_to(map)
    map.save(path_target)
    webbrowser.open(path_target)

def circle_marker_day(df_coor, map, day, df_dic) : 
    for i in range(len(df_coor)):
        folium.CircleMarker(
            location = (df_coor['coordonnées'][i][1],df_coor['coordonnées'][i][0]),
            radius = radius_size(df_dic, day, i),
            color =color_change(df_dic ,map, day, i),
            fill = True,
            fill_color =color_change(df_dic ,map, day, i),
            tooltip= str(df_coor['nom'][i])+' : '+ str(int(df_dic[list(df_dic.keys())[i]]['intensity'][day])),
            # fill_opacity=0.2,
            # line_opacity=0.8
        ).add_to(map)
        print(color_change(df_dic ,map, day, i))

def radius_size(df_dic, day , i):
    rad = df_dic[list(df_dic.keys())[i]]['intensity'][day]*0.025
    return rad

def color_change(df_dic ,map, day, i) :
    cm = branca.colormap.LinearColormap(['yellow', 'darkred'], vmin=0, vmax=3000)
    color = cm(df_dic[list(df_dic.keys())[i]]['intensity'][day]) 
    print(color)
    return color

def time_bar(map,df_dic):
    hm = HeatMapWithTime(df_dic["Beracasa"],auto_play=True,max_opacity=0.8)
    hm.add_to(map)

def color_legend(map):
    linear = cmp.LinearColormap(
    ['yellow', 'orange','red', 'darkred'],
    vmin=0, vmax=3000,
    caption='Nombre de vélo' 
    )
    linear.add_to(map)

