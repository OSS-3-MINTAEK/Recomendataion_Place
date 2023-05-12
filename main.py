from places import places
import pandas as pd

# csv 데이터 불러오기
cafe_data = pd.read_csv('cafe_place_data.csv',encoding='utf-8')
food_data = pd.read_csv('food_place_data.csv',encoding='utf-8')
tour_data = pd.read_csv('tourist_place_data.csv',encoding='utf-8')
walk_data = pd.read_csv('walk_place_data.csv',encoding='utf-8')

# place class 생성 및 초기 설정
place = places(cafe_data)
place.init_place()

# 장소 추천 함수 실행
recommend_places = place.start_recommend()

# 추천 장소 출력
for recommend_place in recommend_places:
    print('장소: ', recommend_place)