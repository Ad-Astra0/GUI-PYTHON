from tkinter import *
from tkinter import messagebox
window=Tk()
window.title("RadioButton")
window.geometry("900x600")
def selectGender():
  gen=gender.get()
  messagebox.showinfo("Gender",gen)
l1=Label(window,text="Select your Gender:")
l1.place(x=100,y=50)
gender=StringVar()
male=Radiobutton(window,variable=gender,text="Male",value="male",command=selectGender)
male.place(x=200, y=75)
female=Radiobutton(window,variable=gender,text="Female",value="female",command=selectGender)
female.place(x=300,y=75)
window.mainloop()



















