import pandas as pd
from geopy.geocoders import Nominatim
from geopy import distance

# csv 데이터 불러오기
cafe_data = pd.read_csv('cafe_place_data.csv', encoding='utf-8')
food_data = pd.read_csv('food_place_data.csv', encoding='utf-8')
tour_data = pd.read_csv('tourist_place_data.csv', encoding='utf-8')
hotel_data = pd.read_csv('hotel_place_data.csv', encoding='utf-8')

def extract_data(data, location):
    result = data[data['지역'].str.contains(location)]
    return result

# 사용자의 위치 입력
locations = ['제주시', '애월읍', '한림읍', '한경면', '대정읍', '인덕면', '중문', '서귀포시', '남원읍', '표선면', '성산읍', '우도', '구좌읍', '조천읍']
print(locations)

while True:
    user_location = input("위치를 입력하세요: ")
    if user_location in locations:
        break

# 사용자의 위치 근처 데이터 추출
near_user_cafe = cafe_data[cafe_data['지역'].str.contains(user_location)]
near_user_food = food_data[food_data['지역'].str.contains(user_location)]
near_user_tour = tour_data[tour_data['지역'].str.contains(user_location)]
near_user_hotel = hotel_data[hotel_data['지역'].str.contains(user_location)]

# 사용자의 위치 위도 경도 불러오기
geolocator = Nominatim(user_agent="geopy")
location = geolocator.geocode(user_location, timeout=None)
if location:
    user_lat, user_lon = location.latitude, location.longitude

# 사용자의 위치와 가게의 거리 차 구하기
def add_distance_row(data, user_lat, user_lon):
    data['거리 차'] = data['위치'].apply(
        lambda x: distance.distance((user_lat, user_lon), geolocator.geocode(x, timeout=None).point).km
        if geolocator.geocode(x) is not None else None)
    
add_distance_row(near_user_cafe, user_lat, user_lon)
add_distance_row(near_user_food, user_lat, user_lon)
add_distance_row(near_user_tour, user_lat, user_lon)
add_distance_row(near_user_hotel, user_lat, user_lon)

# 거리 차가 적은 순으로 정렬하여 상위 5개 추출
result_cafe = near_user_cafe.sort_values(by='거리 차', ascending=True).head(5)[['이름', '거리 차']]
result_food = near_user_food.sort_values(by='거리 차', ascending=True).head(5)[['이름', '거리 차']]
result_tour = near_user_tour.sort_values(by='거리 차', ascending=True).head(5)[['이름', '거리 차']]
result_hotel = near_user_hotel.sort_values(by='거리 차', ascending=True).head(5)[['이름', '거리 차']]

# 결과 출력 함수 정의
def print_results(category, result):
    print(f"--- {category} 순위 ---")
    for i, row in result.iterrows():
        print(f"{i + 1}. {row['이름']}: {row['거리 차']:.4f} km")

# Print the first rank for each category
print_results("Cafe", result_cafe.head(1))
print_results("Food Place", result_food.head(1))
print_results("Tourist Place", result_tour.head(1))
print_results("Hotel", result_hotel.head(1))

current_rank = {
    "Cafe": 1,
    "Food Place": 1,
    "Tourist Place": 1,
    "Hotel": 1
}

while True:
    category_choice = int(input("Enter the category number to view more ranks (cafe : 1, Food : 2, Tourtist : 3, Hotel : 4 or enter '0' to stop): "))

    if category_choice == 0:
        break
    
    if category_choice == 1:
        current_rank["Cafe"] += 1
        print_results("Cafe", result_cafe.iloc[current_rank["Cafe"] - 1:current_rank["Cafe"]])
        print_results("Food Place", result_food.iloc[current_rank["Food Place"] - 1:current_rank["Food Place"]])
        print_results("Tourist Place", result_tour.iloc[current_rank["Tourist Place"] - 1:current_rank["Tourist Place"]])
        print_results("Hotel", result_hotel.iloc[current_rank["Hotel"] - 1:current_rank["Hotel"]])
    elif category_choice == 2:
        current_rank["Food Place"] += 1
        print_results("Cafe", result_cafe.iloc[current_rank["Cafe"] - 1:current_rank["Cafe"]])
        print_results("Food Place", result_food.iloc[current_rank["Food Place"] - 1:current_rank["Food Place"]])
        print_results("Tourist Place", result_tour.iloc[current_rank["Tourist Place"] - 1:current_rank["Tourist Place"]])
        print_results("Hotel", result_hotel.iloc[current_rank["Hotel"] - 1:current_rank["Hotel"]])
    elif category_choice == 3:
        current_rank["Tourist Place"] += 1
        print_results("Cafe", result_cafe.iloc[current_rank["Cafe"] - 1:current_rank["Cafe"]])
        print_results("Food Place", result_food.iloc[current_rank["Food Place"] - 1:current_rank["Food Place"]])
        print_results("Tourist Place", result_tour.iloc[current_rank["Tourist Place"] - 1:current_rank["Tourist Place"]])
        print_results("Hotel", result_hotel.iloc[current_rank["Hotel"] - 1:current_rank["Hotel"]])
    elif category_choice == 4:
        current_rank["Hotel"] += 1
        print_results("Cafe", result_cafe.iloc[current_rank["Cafe"] - 1:current_rank["Cafe"]])
        print_results("Food Place", result_food.iloc[current_rank["Food Place"] - 1:current_rank["Food Place"]])
        print_results("Tourist Place", result_tour.iloc[current_rank["Tourist Place"] - 1:current_rank["Tourist Place"]])
        print_results("Hotel", result_hotel.iloc[current_rank["Hotel"] - 1:current_rank["Hotel"]])
    else:
        print("Invalid input. Please enter a valid category number.")