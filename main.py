import random
from places import places

place = places()


while True:
    input_place = input("장소를 입력하세요 (종료하려면 '끝'을 입력하세요): ")
    if input_place == '끝':
        break
    place.add_place(input_place)

random_value = random.choice(place.get_places())

print("무작위 장소 추천 -", random_value) #무작위로 추천