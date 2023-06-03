import pandas as pd
from geopy.geocoders import Nominatim
from geopy import distance

class Places:
    def __init__(self, food_data, cafe_data, hotel_data, tourist_data):
        self.food_places = food_data
        self.cafe_places = cafe_data
        self.hotel_places = hotel_data
        self.tourist_places = tourist_data
        self.geolocator = Nominatim(user_agent="geopy")

    def convert_address_to_coordinates(self, address, address2):
        try:
            location = self.geolocator.geocode(address)
            if location:
                return location.latitude, location.longitude
            else:
                location = self.geolocator.geocode(address2)
                if location:
                    return location.latitude, location.longitude
        except:
            pass

        return None, None

    def calculate_distance(self, lat1, lon1, lat2, lon2):
        coords_1 = (lat1, lon1)
        coords_2 = (lat2, lon2)
        dist = distance.distance(coords_1, coords_2).kilometers
        return dist

    def compare_distances(self, user_location):
        user_lat, user_lon = self.convert_address_to_coordinates(user_location, user_location)
        if user_lat is None or user_lon is None:
            print("유효하지 않은 사용자 위치입니다.")
            return

        distances = []

        for index, row in self.food_places.iterrows():
            food_lat, food_lon = self.convert_address_to_coordinates(row['위치'], row['지역'])
            if food_lat is not None and food_lon is not None:
                food_distance = self.calculate_distance(user_lat, user_lon, food_lat, food_lon)
                distances.append(('음식점', row['이름'], food_distance))

        for index, row in self.cafe_places.iterrows():
            cafe_lat, cafe_lon = self.convert_address_to_coordinates(row['위치'], row['지역'])
            if cafe_lat is not None and cafe_lon is not None:
                cafe_distance = self.calculate_distance(user_lat, user_lon, cafe_lat, cafe_lon)
                distances.append(('카페', row['이름'], cafe_distance))

        for index, row in self.hotel_places.iterrows():
            hotel_lat, hotel_lon = self.convert_address_to_coordinates(row['위치'], row['지역'])
            if hotel_lat is not None and hotel_lon is not None:
                hotel_distance = self.calculate_distance(user_lat, user_lon, hotel_lat, hotel_lon)
                distances.append(('호텔', row['이름'], hotel_distance))

        for index, row in self.tourist_places.iterrows():
            tourist_lat, tourist_lon = self.convert_address_to_coordinates(row['위치'], row['지역'])
            if tourist_lat is not None and tourist_lon is not None:
                tourist_distance = self.calculate_distance(user_lat, user_lon, tourist_lat, tourist_lon)
                distances.append(('관광지', row['이름'], tourist_distance))

        distances.sort(key=lambda x: x[2])

        print(f"사용자 위치({user_location})와의 가장 가까운 장소:")
        
        for place_type in ['음식점', '카페', '호텔', '관광지']:
            closest_place = next((place for place in distances if place[0] == place_type), None)
            if closest_place:
                print(f"{place_type}: {closest_place[1]}, 거리: {closest_place[2]:.2f} km")
            else:
                print(f"{place_type}: 해당하는 장소 없음")


# CSV 파일 경로
food_csv = 'food_place_data.csv'
cafe_csv = 'cafe_place_data.csv'
hotel_csv = 'hotel_place_data.csv'
tourist_csv = 'tourist_place_data.csv'

# CSV 데이터 로드
food_data = pd.read_csv(food_csv, encoding='utf-8')
cafe_data = pd.read_csv(cafe_csv, encoding='utf-8')
hotel_data = pd.read_csv(hotel_csv, encoding='utf-8')
tourist_data = pd.read_csv(tourist_csv, encoding='utf-8')

# Places 객체 생성
places = Places(food_data, cafe_data, hotel_data, tourist_data)

# 사용자 위치 입력
user_location = input("사용자 위치를 입력하세요: ")

# 사용자 위치와 장소들 사이의 거리 비교
places.compare_distances(user_location)
