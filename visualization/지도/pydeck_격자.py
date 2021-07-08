# EUC-KR 
import geopandas as gpd
import pydeck as pdk
import pandas as pd

def polygon_to_coordinates(x): 
    lon, lat = x.exterior.xy 
    return [[x, y] for x, y in zip(lon, lat)] 

def multipolygon_to_coordinates(x):
    lon, lat = x[0].exterior.xy
    return [[x, y] for x, y in zip(lon, lat)]

def data_fe(data):
    df = gpd.read_file(data, encoding='EUC-KR')
    df["val"] = df["val"].str.replace(pat=r'[^\w]', repl=r'0', regex=True)
    df['val'] = df['val'].astype(float)
    df['coordinates'] = df['geometry'].apply(polygon_to_coordinates)
    del df['geometry']
    df = pd.DataFrame(df)
    df['grid_id']=0
    idx = []
    for i in range(len(df)):
        idx.append(str('종로')+str(i).zfill(2))
    lat_min, lat_max, lon_min, lon_max = [],[],[],[]
    for i in range(len(df)):    
        lon_min.append(df['coordinates'][i][1][0])
        lon_max.append(df['coordinates'][i][3][0])
        lat_min.append(df['coordinates'][i][0][1])
        lat_max.append(df['coordinates'][i][2][1])
    df['lon_min'], df['lon_max'], df['lat_min'], df['lat_max'] = lon_min, lon_max, lat_min, lat_max
    df['grid_id'] = pd.DataFrame(idx)
    df['정규화_시각화']=df['val']/df['val'].max()
    return df

def seoul_fe(data):
    df_seoul = gpd.read_file(data)
    df_seoul['coordinates'] = df_seoul['geometry'].apply(multipolygon_to_coordinates)
    del df_seoul['geometry']
    df_seoul = pd.DataFrame(df_seoul)
    return df_seoul

def plot_grid(data,style):
    layer_poly = pdk.Layer(
     'PolygonLayer',
     df_seoul,
     get_polygon = 'coordinates',
     get_fill_color = '[0,0,0,50]',
     pickable = True,
     auto_highlight = True
    )
    layer1 = pdk.Layer( 'PolygonLayer', 
                  df, 
                  get_polygon='coordinates', 
                  get_fill_color='[227, 255, 227, 80]', 
                  pickable=True, 
                  auto_highlight=True 
                 ) 
    layer = pdk.Layer( 'PolygonLayer', 
                  df, 
                  get_polygon='coordinates', 
                  get_fill_color='[220, 255*정규화_시각화, 227, 1000*정규화_시각화]', 
                  pickable=True, 
                  auto_highlight=True 
                 ) 
    center = [126.931385, 37.4040] 
    view_state = pdk.ViewState( 
        longitude=center[0], 
        latitude=center[1], 
        zoom=9
    )  
    r = pdk.Deck(layers=[layer_poly,layer1,layer], initial_view_state=view_state,
                 map_style= style,
                 mapbox_key = MAPBOX_API_KEY,
                 tooltip={
                 "html": "<b>주소:</b> {grid_id}"
                 "<br/> <b>공시지가:</b> {val}"})
    return r.to_html()
  
MAPBOX_API_KEY = "pk.eyJ1IjoibWpzMTk5NSIsImEiOiJja2pyM3AyZjEwMzZ6MnltdTA4aDc1NjJkIn0.SN28pnAUfydkAeMtp28uMw"
style = 'mapbox://styles/mapbox/outdoors-v11'

data = '종로구_공시지가.geojson'
df = data_fe(data)
df_seoul = seoul_fe('Seoul.geojson')
plot_grid(df,style)

# 경도 위도 표기
def data_fe(data):
    df = gpd.read_file(data, encoding='EUC-KR')
    df['경도'] = df.geometry.centroid.x
    df['위도'] = df.geometry.centroid.y
    df["val"] = df["val"].str.replace(pat=r'[^\w]', repl=r'0', regex=True)
    df['val'] = df['val'].astype(float)
    df['coordinates'] = df['geometry'].apply(polygon_to_coordinates)
    df = pd.DataFrame(df)
    df['grid_id']=0
    idx = []
    for i in range(len(df)):
        idx.append(str('종로')+str(i).zfill(2))
    lat_min, lat_max, lon_min, lon_max = [],[],[],[]
    for i in range(len(df)):    
        lon_min.append(df['coordinates'][i][1][0])
        lon_max.append(df['coordinates'][i][3][0])
        lat_min.append(df['coordinates'][i][0][1])
        lat_max.append(df['coordinates'][i][2][1])
    df['lon_min'], df['lon_max'], df['lat_min'], df['lat_max'] = lon_min, lon_max, lat_min, lat_max
    df['grid_id'] = pd.DataFrame(idx)
    df['정규화_시각화']=df['val']/df['val'].max()
    return df
