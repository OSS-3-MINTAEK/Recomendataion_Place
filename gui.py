from tkinter import *
window=Tk()
def  process():
    tf=float(e1.get()) # e1 엔트리 클래스에서 사용자가 입력한 값을 get 메서드를 통해서 가져옴
    tc=(tf-32.0)*5.0/9.0
    e2.delete(0,END) # e2 엔트리의 값을 처음부터 끝까지 
    
Label(window,text="제주도 장소 추천").grid(row=0)
label=Label(window,text="사용자의 위치를 입력하세요.").grid(row=1)

put=Entry(window).grid(row=1,column=1)
Label(window,text="장소1:").grid(row=3,column=0)
Label(window,text="장소2:").grid(row=4,column=0)
Label(window,text="장소3:").grid(row=5,column=0)

e1=Entry(window).grid(row=3,column=1)
e2=Entry(window).grid(row=4,column=1)
e3=Entry(window).grid(row=5,column=1)
Button(window,text="변경").grid(row=3,column=2)
Button(window,text="변경").grid(row=4,column=2)
Button(window,text="변경").grid(row=5,column=2)
window.mainloop()