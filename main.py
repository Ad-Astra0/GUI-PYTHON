import math
from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("Form")
window.geometry("600x400")
def selectMATH():
  t=m.get()
  s1=int(t1.get("1.0",END))
  if(t=="square"):
    answer=s1*s1
    l3.config(text=str(answer))
  elif(t=="cube"):
    answer=s1*s1*s1
    l3.config(text=str(answer))
  elif(t=="root"):
    answer=math.sqrt(s1)
    l3.config(text=str(answer))
  
m=StringVar()
Squared=Radiobutton(window,variable=m,text="Squared",value="square",command=selectMATH)
Squared.place(x=100, y=300)
Cubed=Radiobutton(window,variable=m,text="Cubed",value="cube",command=selectMATH)
Cubed.place(x=200,y=300)
Squareroot=Radiobutton(window,variable=m,text="Square root",value="root",command=selectMATH)
Squareroot.place(x=300,y=300)

l1=Label(window,text='Number',bg='green',fg='white',height=2)
l1.place(x=100,y=100)
t1=Text(window,height=2,width=20)
t1.place(x=250,y=100)
l2=Label(window,text='Answer',bg='green',fg='white',height=2)
l2.place(x=100,y=200)
l3=Label(window,text='',height=2)
l3.place(x=200,y=200)

window.mainloop()