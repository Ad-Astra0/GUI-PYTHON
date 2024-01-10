from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("TikTackToe")
window.geometry("600x400")
def Analysis():
  h=0
  l=0
  if(g.get()=="yes"):
    h+=1
  elif(g.get()=="no"):
    l+=1
  if(j.get()=="yes"):
    l+=1
  elif(j.get()=="no"):
    h+=1
  if(x.get()=="yes"):
    l+=1
  elif(x.get()=="no"):
    h+=1
  if(z.get()=="yes"):
    h+=1
  elif(z.get()=="no"):
    l+=1
  if(c.get()=="yes"):
    h+=1
  elif(c.get()=="no"):
    l+=1
  if(h>l):
    messagebox.showinfo(title="Result", message="Higher Risk for Heart Diease")
  elif(l>h):
    messagebox.showinfo(title="Result", message="Lower Risk for Heart Diease")
  
g=StringVar()
Yes1=Radiobutton(window,variable=g,text="Yes",value="yes")
Yes1.place(x=450, y=100)
No1=Radiobutton(window,variable=g,text="No",value="no")
No1.place(x=500,y=100)
j=StringVar()
Yes2=Radiobutton(window,variable=j,text="Yes",value="yes")
Yes2.place(x=450, y=150)
No2=Radiobutton(window,variable=j,text="No",value="no")
No2.place(x=500,y=150)
x=StringVar()
Yes3=Radiobutton(window,variable=x,text="Yes",value="yes")
Yes3.place(x=450, y=200)
No3=Radiobutton(window,variable=x,text="No",value="no")
No3.place(x=500,y=200)
z=StringVar()
Yes4=Radiobutton(window,variable=z,text="Yes",value="yes")
Yes4.place(x=450, y=250)
No4=Radiobutton(window,variable=z,text="No",value="no")
No4.place(x=500,y=250)
c=StringVar()
Yes5=Radiobutton(window,variable=c,text="Yes",value="yes",command=Analysis)
Yes5.place(x=450, y=300)
No5=Radiobutton(window,variable=c,text="No",value="no",command=Analysis)
No5.place(x=500,y=300)

l1=Label(window,text='Risk of Heart Diease',bg='green',fg='white',height=2)
l1.place(x=100,y=50)
l2=Label(window,text='Are you over your wieght for your age',bg='grey',fg='white',height=2)
l2.place(x=100,y=100)
l3=Label(window,text='Do you eat healthy?',height=2)
l3.place(x=100,y=150)
l4=Label(window,text='Do you exercise more than two to three times a week?',bg='grey',fg='white',height=2)
l4.place(x=100,y=200)
l5=Label(window,text='Do you feel very stressful everyday?',bg='grey',fg='white',height=2)
l5.place(x=100,y=250)
l6=Label(window,text='Does heart diease run in your family?',bg='grey',fg='white',height=2)
l6.place(x=100,y=300)
window.mainloop()