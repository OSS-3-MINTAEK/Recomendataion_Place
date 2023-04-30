import random

places = []

while True:
    place = input("장소를 입력하세요 (종료하려면 '끝'을 입력하세요): ")
    if place == '끝':
        break
    places.append(place)

random_value = random.choice(places)

print("무작위 장소 추천 -", random_value) #무작위로 추천