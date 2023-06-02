#from places import Places는 "places"라는 모듈에서 "Places"라는 클래스를 가져옵니다. 
#import pandas as pd는 "pandas"라이브러리를 가져옵니다. pandas는 데이터 조작과 분석을 위한 강력한 도구로 널리 사용됩니다.
#from tkinter import *는 "tkinter"라이브러리를 가져옵니다. tkinter는 Python에서 GUI (그래픽 사용자 인터페이스)를 구축하기 위한 표준 라이브러리입니다. 
from places import Places
import pandas as pd
from tkinter import *
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
