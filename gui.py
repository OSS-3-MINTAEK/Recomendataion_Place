from tkinter import *
window=Tk()

Label(window,text="제주도 장소 입력:").grid(row=0)

e1=Entry(window)


e1.grid(row=0,column=1)

# photo=PhotoImage(file="jeju.png")
# label=Label(window,image=photo)
# label.grid()
window.mainloop()
