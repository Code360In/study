# 6.24
# import
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pydeck as pdk

# SETTING PAGE CONFIG TO WIDE MODE
st.set_page_config(layout="wide")

# LOADING DATA
DATE_TIME = "date/time"
DATA_URL = (
    "http://s3-us-west-2.amazonaws.com/streamlit-demo-data/uber-raw-data-sep14.csv.gz"
)

# CREATING FUNCTION FOR MAPS
def map(data, lat, lon, zoom):
    st.write(pdk.Deck(
        map_style="mapbox://styles/mapbox/light-v9",
        initial_view_state={
            "latitude": lat,
            "longitude": lon,
            "zoom": zoom,
            "pitch": 50,
        },
        layers=[
            pdk.Layer(
                "HexagonLayer",
                data=data,
                get_position=["lon", "lat"],
                radius=100,
                elevation_scale=4,
                elevation_range=[0, 1000],
                pickable=True,
                extruded=True,
            ),
        ]
    ))

# 맨위 좌우로 지정!! row칼럼!!
# LAYING OUT THE TOP SECTION OF THE APP
row1_1, row1_2 = st.beta_columns((2,3))

with row1_1:
    st.title("NYC Uber Ridesharing Data")
    hour_selected = st.slider("Select hour of pickup", 0, 23)

with row1_2:
    st.write(
    """
    ##
    Examining how Uber pickups vary over time in New York City's and at its major regional airports.
    By sliding the slider on the left you can view different slices of time and explore different transportation trends.
    """)

# FILTERING DATA BY HOUR 
SELECTED - 시간필터링
data = data[data[DATE_TIME].dt.hour == hour_selected]

# LAYING OUT THE MIDDLE SECTION OF THE APP WITH THE MAPS - 몇개를 보여줄것인가?
row2_1, row2_2, row2_3, row2_4 = st.beta_columns((2,1,1,1))

# SETTING THE ZOOM LOCATIONS FOR THE AIRPORTS
la_guardia= [40.7900, -73.8700]
jfk = [40.6650, -73.7821]
newark = [40.7090, -74.1805]
zoom_level = 12
midpoint = (np.average(data["lat"]), np.average(data["lon"]))

with row2_1:
    st.write("**All New York City from %i:00 and %i:00**" % (hour_selected, (hour_selected + 1) % 24))
    map(data, midpoint[0], midpoint[1], 11)

with row2_2:
    st.write("**La Guardia Airport**")
    map(data, la_guardia[0],la_guardia[1], zoom_level)

with row2_3:
    st.write("**JFK Airport**")
    map(data, jfk[0],jfk[1], zoom_level)

with row2_4:
    st.write("**Newark Airport**")
    map(data, newark[0],newark[1], zoom_level)

## 2열 그래프 작성완료
## 3열
# FILTERING DATA FOR THE HISTOGRAM
filtered = data[
    (data[DATE_TIME].dt.hour >= hour_selected) & (data[DATE_TIME].dt.hour < (hour_selected + 1))
    ]

hist = np.histogram(filtered[DATE_TIME].dt.minute, bins=60, range=(0, 60))[0]

chart_data = pd.DataFrame({"minute": range(60), "pickups": hist})
### 차트 데이터를 여기에 저장

# LAYING OUT THE HISTOGRAM SECTION

st.write("")

st.write("**Breakdown of rides per minute between %i:00 and %i:00**" % (hour_selected, (hour_selected + 1) % 24))

st.altair_chart(alt.Chart(chart_data)
    .mark_area(
        interpolate='step-after',
    ).encode(
        x=alt.X("minute:Q", scale=alt.Scale(nice=False)),
        y=alt.Y("pickups:Q"),
        tooltip=['minute', 'pickups']
    ).configure_mark(
        opacity=0.5,
        color='red'
    ), use_container_width=True)


# 6.23
# Kaggle kernel
## Visualization map using Folium 
## Visualization map using plotly 
## Visualization map using Pydeck 
## Visualization Dashboard using Dash

# JupyterHub
- https://jupyterhub.readthedocs.io/en/stable/index.html
- https://cdsdashboards.readthedocs.io/en/stable/

# Volia Jupyter Notebook
- https://ichi.pro/ko/voilaleul-sayonghayeo-jupyter-noteubug-eseo-daehwa-hyeong-daesi-bodeu-mandeulgi-200425063371098

# streamlit & pdk 
import streamlit as st
import pydeck as pdk

https://github.com/nikkisharma536/streamlit_app/blob/master/covid_data.py

## pydeck - mapbox style
map_style = 'mapbox://styles/mapbox/outdoors-v11'

## FE - 원하는 데이터 찾기
test = df_cois.loc[df_cois['버스정류장ARS번호'].isin(arss)]
n_of_stops = len(df_cois.loc[df_cois['버스정류장ARS번호'].isin(arss)]['버스정류장ARS번호'].unique())


## pydeck - 경로선 시각화
layer_path = pdk.Layer(
    'PathLayer',
    bus_road,
    get_path='lines',
    get_width = '80',
    get_color='[139,69,19]',
    pickable=True,
    auto_highlight=True
)


## pydeck 
변수 : 편의점 상호명 adm_cd 경도 위도
df_7 = df_s[df_s['편의점'] == '세븐일레븐']
df_7.reset_index()
df_C = df_s[df_s['편의점'] == 'CU']
df_C.reset_index()
df_G = df_s[df_s['편의점'] == 'GS']
df_G.reset_index()
df_M = df_s[df_s['편의점'] == '미니스톱']
df_M.reset_index()


layer_poly = pdk.Layer(
 'PolygonLayer',
 df,
 get_polygon = 'coordinates',
 get_fill_color = '[0,0,0,50]',
 pickable = True,
 auto_highlight = True
)
layer_7 = pdk.Layer(
 'ScatterplotLayer',
 df_7
 get_position = '[경도, 위도]',
 get_radius = 100,
 get_fill_color = '[255,0,0]',
 pickable = True
 auto_highlight = True
)
layer_C = pdk.Layer(
 'ScatterplotLayer',
 df_C
 get_position = '[경도, 위도]',
 get_radius = 100,
 get_fill_color = '[189,27,33,255]',
 pickable = True
 auto_highlight = True
)
layer_G = pdk.Layer(
 'ScatterplotLayer',
 df_G
 get_position = '[경도, 위도]',
 get_radius = 100,
 get_fill_color = '[189,27,33,255]',
 pickable = True
 auto_highlight = True
)
layer_M = pdk.Layer(
 'ScatterplotLayer',
 df_M
 get_position = '[경도, 위도]',
 get_radius = 100,
 get_fill_color = '[189,27,33,255]',
 pickable = True
 auto_highlight = True
)

r = pdk.Deck(layers=[layer_poly, layer_7 , layer_C, layer_G, layer_M ],
            map_style='mapbox://styles/mapbox/outdoors-v11',
            mapbox_key = API키,
            initial_view_state = view_state)
r.to_html()


# 업종별 데이터 
- G유동인구(성별 / 시간대별 보행 인구, 낮 상주/밤 상주 인구수)
- 인구정보 : 소멸위험지수 사용! 시군구 기반 -> 행정동??
- G기상 데이터 : 대기오염( 미세먼지 / 초미세먼지 / 오존 / 이산화질소 / 아황산가스 / 일산화탄소) 
- 카드 데이터 : 매출, 
- 건물정보 : 총 주차수 / 공시지가 / 건물 내 프렌차이즈 사업체 목록
- 500미터 내 마트 개수 / 백화점 개수/ 편의점 개수 / 카페,학원,세탁소 개수 

# 외부데이터
## 경기 버스 정보 : 서울시는?? (http://www.gbis.go.kr/) 
[route] GGD_RouteInfo_M.xls : 버스 노선 정보 (기점, 종점 / 주중배차간격, 주말배차간격 / 첫차, 막차 시간)
[trans] GGD_RouteStationInfo_M.xls : 노선 경유 정보 (버스 노선 순서)
-> 주중배차간격/ 주말 배차간격 / 상_하행 첫차 막차 / 상행/하행운행시간 
-> 전체 승하차 건수 / 승차많은버스 / 환승많은버스 / 하차많은버스 / 버스정류장운행시간 

## 기상데이터 
- 일자별 기상 데이터 : 기상자료개방포털 > 종관기상관측 (ASOS)
https://data.kma.go.kr/data/grnd/selectAsosRltmList.do?pgmNo=36
- 일자별 미세먼지 데이터 : 에어코리아 > 시도별 대기정보 (PM2.5 & PM10)
https://www.airkorea.or.kr/web/sidoQualityCompare?itemCode=10008&pMENU_NO=102
- 결측값 0 
- 최저/최고기온 

## 지하철
- 500m내 지하철역갯수
- 지하철이용객 

## 실거래가_국토교통부
http://rtdown.molit.go.kr/
- 위경도 변환
주소 좌표 변환 툴 Geocoder-Xr 을 사용해 위경도 정보 추출(http://www.gisdeveloper.co.kr/?p=4784)
- 건축년도 / 전용면적/ 층 / 거래금액/ 면적당금액 

## 유동인구
- 출퇴근 유동인구
- 성연령별 유동인구 
- 요일별 유동인구(주중,주말 평균)
- 디지털 정보화 지수(10대~60대)
https://www.nia.or.kr/site/nia_kor/ex/bbs/View.do?cbIdx=81623&bcIdx=23112&parentSeq=23112

## 상권 데이터
출처 : 공공데이터포털 소상공인시장진흥공단_상가(상권)정보_경기

## 상권 원하는 부분만 가져오는 코드
store = pd.read_excel(current_path+'/data/store_info.xlsx')

# 수원 데이터만 가져오기 
loc_code = list(df_30["EMD_CD"].astype(float) * 100)  # 수원시 법정동 코드 목록 

suwon_store = store[store["법정동코드"].isin(loc_code)]
print(suwon_store.shape)
---
print('커피전문점/카페/다방', ":", suwon_store[suwon_store.상권업종소분류명 == '커피전문점/카페/다방'].shape[0])

print('편의점', ":", suwon_store[(suwon_store.상권업종소분류명 == '편의점') & (suwon_store.상호명.str.contains('GS25|세븐일레븐|CU'))].shape[0] + \
      suwon_store[(suwon_store.상호명.str.contains('이마트')) & (suwon_store.지점명.str.contains('24'))].shape[0] + \
      suwon_store[suwon_store.상호명 == '이마트24'].shape[0])

print('학원', ":", suwon_store[suwon_store.상권업종중분류명 == '학원-보습교습입시'].shape[0] + \
      suwon_store[suwon_store.상권업종중분류명 == '학원-어학'].shape[0])

print('세탁소/빨래방', ":", suwon_store[suwon_store.상권업종소분류명 == '세탁소/빨래방'].shape[0], '\n')

# 마트 
print('이마트' , ":", suwon_store[(suwon_store.지점명.str.contains('24') == False) & (suwon_store.상호명 == '이마트')].shape[0])
print('홈플러스' , ":", suwon_store[suwon_store.상호명 == '홈플러스'].shape[0])
print('롯데마트' , ":", suwon_store[suwon_store.상호명 == '롯데마트'].shape[0])
print('하나로마트' , ":", suwon_store[suwon_store.상호명 == '하나로마트'].shape[0], '\n')

# 백화점 
print('AK플라자' , ":", suwon_store[suwon_store.상호명 == 'AK플라자백화점'].shape[0])
print('NC백화점' , ":", suwon_store[(suwon_store.상호명 == 'NC백화점') & (suwon_store.지점명 == 'NC터미널점')].shape[0])
print('갤러리아백화점' , ":", suwon_store[suwon_store.상호명 == '갤러리아백화점'].shape[0])
print('롯데몰' , ":", suwon_store[suwon_store.상호명 == '롯데몰'].shape[0])
---
mart = pd.concat([suwon_store[(suwon_store.지점명.str.contains('24') == False) & (suwon_store.상호명 == '이마트')], 
                  suwon_store[suwon_store.상호명 == '홈플러스'], suwon_store[suwon_store.상호명 == '롯데마트'], 
                  suwon_store[suwon_store.상호명 == '하나로마트']], axis=0)

dep = pd.concat([suwon_store[suwon_store.상호명 == 'AK플라자백화점'], 
                 suwon_store[(suwon_store.상호명 == 'NC백화점') & (suwon_store.지점명 == 'NC터미널점')], 
                 suwon_store[suwon_store.상호명 == '갤러리아백화점'], suwon_store[suwon_store.상호명 == '롯데몰']] , axis=0)

conv = pd.concat([suwon_store[(suwon_store.상권업종소분류명 == '편의점') & (suwon_store.상호명.str.contains('GS25|세븐일레븐|CU'))], 
                  suwon_store[(suwon_store.상호명.str.contains('이마트')) & (suwon_store.지점명.str.contains('24'))], 
                  suwon_store[suwon_store.상호명 == '이마트24']], axis=0)

cafe = suwon_store[suwon_store.상권업종소분류명 == '커피전문점/카페/다방']

academy = pd.concat([suwon_store[suwon_store.상권업종중분류명 == '학원-보습교습입시'],
                     suwon_store[suwon_store.상권업종중분류명 == '학원-어학']], axis=0)

laundry = suwon_store[suwon_store.상권업종소분류명 == '세탁소/빨래방']


mart.shape, dep.shape, conv.shape, cafe.shape, academy.shape, laundry.shape
---
def close_store(bus, store, column) : 
    for i in tqdm(range(len(bus))) : 
        distance = [] 
        for j in range(len(store)) : 
            stationloc = tuple(bus[['lon','lat']].iloc[i])
            storeloc = tuple(store[['경도','위도']].iloc[j])
            distance.append(haversine(stationloc, storeloc, unit = 'm'))
            
        distance = [d for d in distance if d <= 500] 
        bus[column][i] = len(distance)
        
    return bus
---
def close_store2(bus, store, column):
    # 각 정류장에 대해 반복
    for i in tqdm(range(len(bus))):
        
        distance = []
        
        # 계산량을 줄이기 위한 filter
        ## lon
        # sort_lon = store.sort_values(by = ['lon']).reset_index(drop = True)
        idx_lon = bisect_left(store['경도'], bus['lon'][i])
        if 1 < idx_lon < len(store) : 
            fltr_lon = store[(store['경도']<store.loc[idx_lon, '경도']+0.001)&(store['경도']>store.loc[idx_lon, '경도']-0.001)].reset_index(drop = True)
            ## lat
            sort_lat = fltr_lon.sort_values(by = ['위도']).reset_index(drop = True)
            idx_lat = bisect_left(sort_lat['위도'], bus['lat'][i])
            
            if 1 < idx_lat < len(sort_lat) : 
                fltr_lat = sort_lat[(sort_lat['위도']<sort_lat.loc[idx_lat, '위도']+0.01)&(sort_lat['위도']>sort_lat.loc[idx_lat, '위도']-0.01)].reset_index(drop = True)

                # filter된 데이터의 거리 계산
                for j in range(len(fltr_lat)):
                    bus_name = tuple(bus[['lon','lat']].iloc[i])
                    fltr_name = tuple(fltr_lat[['경도','위도']].iloc[j])
                    distance.append(haversine(bus_name, fltr_name, unit = 'm'))
        
        distance = [d for d in distance if d <= 500]
            
        if len(distance) > 0 : 
            bus[column][i] = len(distance)
        else : 
            bus[column][i] = 0 
        
    return bus
---
busdf["500미터내마트개수"], busdf["500미터내백화점개수"] = 0, 0
busdf = close_store(busdf, mart, "500미터내마트개수")
busdf = close_store(busdf, dep, "500미터내백화점개수")
conv = conv.sort_values(by = ['경도']).reset_index(drop = True)
cafe = cafe.sort_values(by = ['경도']).reset_index(drop = True)
academy = academy.sort_values(by = ['경도']).reset_index(drop = True)
laundry = laundry.sort_values(by = ['경도']).reset_index(drop = True)

busdf["500미터내편의점개수"], busdf["500미터내카페개수"], busdf["500미터내학원개수"], busdf["500미터세탁소개수"] = 0, 0, 0, 0
busdf = close_store2(busdf, conv, "500미터내편의점개수")
busdf = close_store2(busdf, cafe, "500미터내카페개수") 
busdf = close_store2(busdf, academy, "500미터내학원개수") 
busdf = close_store2(busdf, laundry, "500미터세탁소개수")


# folium maker
- https://www.geeksforgeeks.org/python-adding-markers-to-volcano-locations-using-folium-package/

- https://compas.lh.or.kr/subj/past/code?subjNo=SBJ_2102_002&teamNo=1123

# 데이터 FE / 원하는 변수 조회 추출 
https://compas.lh.or.kr/subj/past/code?subjNo=SBJ_2102_002&teamNo=1077

# 빅데이터 분석 로컬푸드 DT
https://yongku.tistory.com/entry/%EB%B9%85%EB%8D%B0%EC%9D%B4%ED%84%B0-%EB%B6%84%EC%84%9D-%EB%A1%9C%EC%BB%AC%ED%91%B8%EB%93%9C-DT-%EC%9E%85%EC%A7%80-%EC%84%A0%EC%A0%95-%ED%94%84%EB%A1%9C%EC%A0%9D%ED%8A%B8

# folium
m = folum.map(~)
for index, row in df.iterrows():
    folium.Marker([row['LATITUDE_위도'], row['LONGITUDE_경도']], icon=folium.Icon(icon = 'flag', color = 'green')).add_to(m)

for index, row in df2.iterrows():
    folium.Marker([row['LATITUDE_위도'], row['LONGITUDE_경도']], icon=folium.Icon(icon = 'star', color = 'blue')).add_to(m)

for index, row in df3.iterrows():
    folium.Marker([row['LATITUDE_위도'], row['LONGITUDE_경도']], icon=folium.Icon(icon = 'bookmark', color = 'orange')).add_to(m)
m    
