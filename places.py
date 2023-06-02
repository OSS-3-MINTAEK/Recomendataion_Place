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

    def init_all(self):
        self.init_cafe_place()
        self.init_food_place()
        self.init_tourist_place()

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
    
    def print_recommeded_places(self):
        for recommend_place in self.recommended_place:
            print('장소: ', recommend_place)

    def start_recommend(self):
        # 추천 장소 리셋
        self.recommended_place.clear()

        # 추천 카페 랜덤 선택
        random_cafe = random.choice(self.cafe_places_name)

        # 추천 음식점 랜덤 선택
        random_food = random.choice(self.food_places_name)

        # 추천 관광지 랜덤 선택
        random_tourist = random.choice(self.tourist_places_name)

        # 추천 장소 리스트에 추가
        self.recommended_place.append(random_cafe)
        self.recommended_place.append(random_food)
        self.recommended_place.append(random_tourist)

        # 사용자에게 물어보기
        while True:
            self.print_recommeded_places()
            check = self.user_check()
            if check == True:
                break

        # 리턴
        return self.recommended_place
    
    def user_check(self):
        true_false = False
        check = input("Do you want to change the place? (yes / no) ")
        if check == "yes":
            change_type = input("Which place do you want to change? (cafe / restaurant / tour) ")
            if change_type == "cafe":
                self.recommended_place[0] = random.choice(self.cafe_places_name)
            elif change_type == "restaurant":
                self.recommended_place[1] = random.choice(self.food_places_name)
            elif change_type == "tour":
                self.recommended_place[2] = random.choice(self.tourist_places_name)
            else:
                print("Invalid input.Please choose either 'cafe', 'restaurant', or 'tour'.")
        elif check == "no":
            print("keep it")
            true_false = True
        else:
            print("Invalid input. Please enter either 'yes' or 'no'.")
        return true_false
    
    # 데이터 파일 경로
cafe_data = 'cafe_place_data.csv'
food_data = 'food_place_data.csv'
tourist_data = 'tourist_place_data.csv'
