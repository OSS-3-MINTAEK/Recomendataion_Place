import random
from places import places
import pandas as pd
import numpy as np

data = pd.read_csv('place_data.csv',encoding='utf-8')

place = places(data)
place.init_place()

random_value = random.choice(place.get_places())

print("무작위 장소 추천 -", random_value) #무작위로 추천