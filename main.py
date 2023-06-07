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
locations = ['제주시', '애월읍', '한림읍', '한경면', '대정읍', '인덕면', '중문', '서귀포시', '남원읍', '표선면', '성산읍', '우도', '구좌읍', '조천읍']
print(locations)

while True:
    user_location = input("위치를 입력하세요: ")
    if user_location in locations:
        break

# 데이터 불러오기
data = {}
for category, file_path in data_files.items():
    data[category] = pd.read_csv(file_path, encoding='utf-8')

# 사용자 위치 정보 가져오기
geolocator = Nominatim(user_agent="geopy")
location = geolocator.geocode(user_location, timeout=None)
if location:
    user_lat, user_lon = location.latitude, location.longitude
else:
    raise ValueError("유효하지 않은 위치입니다.")

# 거리 계산 함수 정의
def calculate_distance(point):
    return distance.distance((user_lat, user_lon), point).km

# 사용자 위치 근처 데이터 추출 및 거리 계산
nearby_data = {}
for category, df in data.items():
    nearby_data[category] = df[df['지역'].str.contains(user_location)].copy()
    nearby_data[category]['거리 차'] = nearby_data[category]['위치'].apply(
        lambda x: calculate_distance(geolocator.geocode(x).point) if geolocator.geocode(x) is not None else None
    )

# 결과 출력 함수 정의
def print_results(category, result):
    print(f"--- {category} 순위 ---")
    for i, row in result.iterrows():
        print(f"{i + 1}. {row['이름']}: {row['거리 차']:.4f} km")

# 결과 추출
while True:
    try:
        category = input("확인 하고 싶은 항목을 입력하세요 (카페, 음식점, 관광지, 호텔): ")
        
        if category not in data:
            print("잘못된 입력입니다. 다시 시도해주세요.")
            continue

        result = nearby_data[category].sort_values(by='거리 차', ascending=True).head(5)[['이름', '거리 차']]
        print_results(category, result)
        
    except ValueError:
        print("잘못된 입력입니다. 다시 시도해주세요.")

    row_number = int(input("몇번째 순위를 보고싶은지 입력해주세요 (1~5 입력, 0을 입력하면 종료): "))
    
    if row_number == 0:
        break
    
    try:
        row = result.iloc[row_number - 1]
        print(f"{category} '{row['이름']}'은/는 {row['거리 차']:.4f} km 만큼 {user_location}로부터 떨어져있습니다.")
    
    except IndexError:
        print("잘못된 입력입니다. 다시 시도해주세요.")
