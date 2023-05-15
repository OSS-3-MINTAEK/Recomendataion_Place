import pandas as pd
import random

class Places:
    def __init__(self, cafe_data, food_data, tourist_data):
        self.cafe_places_name = []
        self.food_places_name = []
        self.tourist_places_name = []
        self.recommended_place = []
        self.cafe_data = cafe_data
        self.food_data = food_data
        self.tourist_data = tourist_data

    def init_cafe_place(self):
        place_name = self.cafe_data['이름'].values
        for name in place_name:
            self.add_cafe_place(name)

    def init_food_place(self):
        place_name = self.food_data['이름'].values
        for name in place_name:
            self.add_food_place(name)

    def init_tourist_place(self):
        place_name = self.tourist_data['이름'].values
        for name in place_name:
            self.add_tourist_place(name)

    def add_cafe_place(self, name):
        self.cafe_places_name.append(name)

    def add_food_place(self, name):
        self.food_places_name.append(name)

    def add_tourist_place(self, name):
        self.tourist_places_name.append(name)

    def get_cafe_places(self):
        return self.cafe_places_name

    def get_food_places(self):
        return self.food_places_name

    def get_tourist_places(self):
        return self.tourist_places_name

    def start_recommend(self):
        # 추천 장소 리셋
        self.recommended_place.clear()

        # 추천 카페 랜덤 선택
        random_cafe = random.choice(self.cafe_places_name)

        # 사용자에게 물어보기
        print("Check recommendation place: ", random_cafe)
        random_cafe = self.user_check(self.cafe_places_name, random_cafe)

        # 추천 음식점 랜덤 선택
        random_food = random.choice(self.food_places_name)

        # 추천 관광지 랜덤 선택
        random_tourist = random.choice(self.tourist_places_name)

        # 추천 장소 리스트에 추가
        self.recommended_place.append(random_cafe)
        self.recommended_place.append(random_food)
        self.recommended_place.append(random_tourist)

        # 리턴
        return self.recommended_place
    
    def user_check(self, data, choice_place):
        check = int(input('Agree: 1, Disagree: 2 ='))
        if check == 2:
            random_data = random.choice(data)
            return random_data
        else:
            return choice_place
