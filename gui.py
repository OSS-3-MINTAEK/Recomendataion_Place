from tkinter import *
import pandas as pd
from geopy.geocoders import Nominatim
from geopy import distance

# csv 데이터 불러오기
cafe_data = pd.read_csv('cafe_place_data.csv', encoding='utf-8')
food_data = pd.read_csv('food_place_data.csv', encoding='utf-8')
tour_data = pd.read_csv('tourist_place_data.csv', encoding='utf-8')
hotel_data = pd.read_csv('hotel_place_data.csv', encoding='utf-8')

window=Tk()
def  process():
    tc=put.get()
    
    e2.delete(0,END) # e2 엔트리의 값을 처음부터 끝까지 
    e2.insert(0,tc)

# 위치 입력 받는 곳
Label(window,text="제주도 장소 추천").grid(row=0)
label=Label(window,text="사용자의 위치를 입력하세요.")
label.grid(row=1)
put=Entry(window)
put.grid(row=1,column=1)
Button(window,text="입력",command=process).grid(row=1,column=2)

Label(window,text="장소1:").grid(row=3,column=0)
Label(window,text="장소2:").grid(row=4,column=0)
Label(window,text="장소3:").grid(row=5,column=0)

e1=Entry(window)
e2=Entry(window)
e3=Entry(window)
e1.grid(row=3,column=1)
e2.grid(row=4,column=1)
e3.grid(row=5,column=1)
Button(window,text="변경").grid(row=3,column=2)
Button(window,text="변경").grid(row=4,column=2)
Button(window,text="변경").grid(row=5,column=2)
window.mainloop()