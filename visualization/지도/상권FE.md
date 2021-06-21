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
