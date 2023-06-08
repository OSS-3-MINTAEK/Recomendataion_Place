import pandas as pd
from geopy.geocoders import Nominatim
from geopy import distance

# 데이터 파일 경로
data_files = {
    '카페': 'cafe_place_data.csv',
    '음식점': 'food_place_data.csv',
    '관광지': 'tourist_place_data.csv',
    '호텔': 'hotel_place_data.csv'
}

# 사용자 위치 입력 및 유효성 검사
locations = ['제주시', '애월읍', '한림읍', '한경면', '대정읍', '안덕면', '중문', '서귀포시', '남원읍', '표선면', '성산읍', '우도', '구좌읍', '조천읍']
print(locations)

# 사용자 위치 입력
user_location = input("사용자 위치를 입력하세요: ")

# 유효성 검사
while user_location not in locations:
    print("유효하지 않은 위치입니다. 다시 입력해주세요.")
    user_location = input("사용자 위치를 입력하세요: ")

# 데이터 프레임 로드 및 '위치' 컬럼 추출
df_list = []
for place_type, file_path in data_files.items():
    df = pd.read_csv(file_path)
    df['Place Type'] = place_type
    df_list.append(df)

combined_df = pd.concat(df_list, ignore_index=True)
locations_df = combined_df[['Place Type', '위치']]

# 사용자 위치와 가장 가까운 장소 출력
geolocator = Nominatim(user_agent="place_finder")
user_coordinates = geolocator.geocode(user_location)

if user_coordinates is not None:
    user_coordinates = user_coordinates.point

    closest_places = []

    for place_type in data_files.keys():
        place_df = locations_df[locations_df['Place Type'] == place_type].copy()

        place_df.loc[:, 'Distance'] = place_df['위치'].apply(
            lambda x: distance.distance(user_coordinates, geolocator.geocode(x).point).km if geolocator.geocode(x) is not None else None
        )

        closest_place = place_df.dropna(subset=['Distance']).sort_values(by='Distance').iloc[0]
        closest_places.append(closest_place)

    closest_places_df = pd.DataFrame(closest_places)
    for index, row in closest_places_df.iterrows():
        print(f"{row['Place Type']}: {row['위치']} (거리: {row['Distance']:.2f}km)")
else:
    print("사용자 위치를 찾을 수 없습니다.")
