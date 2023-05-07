import random
class places:
    def __init__(self, data):
        self.places_name = []
        self.recommended_place = []
        self.data = data

    def init_place(self):
        place_name = self.data['장소 이름'].values
        for name in place_name:
            self.add_place(name)

    def add_place(self, name):
        self.places_name.append(name)

    def get_places(self):
        return self.places_name
    
    def start_recommend(self):
        # 추천 장소 리셋
        self.recommended_place.clear()

        # 추천 장소 랜덤 선택
        random_cafe = random.choice(self.data[self.data['종류'] == '카페']['장소 이름'].values)
        random_restaurant = random.choice(self.data[self.data['종류'] != '카페']['장소 이름'].values)

        # 추천 장소 리스트에 추가
        self.recommended_place.append(random_restaurant)
        self.recommended_place.append(random_cafe)

        # 리턴
        return self.recommended_place