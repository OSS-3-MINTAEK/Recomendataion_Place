from places import Places
import pandas as pd
from tkiner import *
# csv 데이터 불러오기
cafe_data = pd.read_csv('cafe_place_data.csv',encoding='utf-8')
food_data = pd.read_csv('food_place_data.csv',encoding='utf-8')
tour_data = pd.read_csv('tourist_place_data.csv',encoding='utf-8')

# place class 생성 및 초기 설정
place = Places(cafe_data, food_data, tour_data)
place.init_all()

# 사용자의 위치 입력
user_location = input("Enter a location: ")

# 장소 추천 함수 실행
recommend_places = place.start_recommend()

# 추천 장소 출력
print(f"\nRecommended places in {user_location}")
for recommend_place in recommend_places:
    print('최종 장소: ', recommend_place)
