from tkinter import *
from tkinter import messagebox
window = Tk()
window.title("TikTackToe")
window.geometry("600x400")
def Buttons1Clicked():
  if b1.cget("text")=="-" and checkforwin()==False:
    b1.config(text=turn.cget("text"))
    something()
    
def Buttons2Clicked():
  if b2.cget("text")=="-"and checkforwin()==False:
    b2.config(text=turn.cget("text"))
    something()
    
def Buttons3Clicked():
  if b3.cget("text")=="-"and checkforwin()==False:
    b3.config(text=turn.cget("text"))
    something()
    
def Buttons4Clicked():
  if b4.cget("text")=="-"and checkforwin()==False:
    b4.config(text=turn.cget("text"))
    something()
    
def Buttons5Clicked():
  if b5.cget("text")=="-"and checkforwin()==False:
    b5.config(text=turn.cget("text"))
    something()
    
def Buttons6Clicked():
  if b6.cget("text")=="-"and checkforwin()==False:
    b6.config(text=turn.cget("text"))
    something()
    
def Buttons7Clicked():
  if b7.cget("text")=="-"and checkforwin()==False:
    b7.config(text=turn.cget("text"))
    something()
    
def Buttons8Clicked():
  if b8.cget("text")=="-"and checkforwin()==False:
    b8.config(text=turn.cget("text"))
    something()
    
def Buttons9Clicked():
  if b9.cget("text")=="-"and checkforwin()==False:
    b9.config(text=turn.cget("text"))
    something()

def something():
  if(checkforwin()==True):
    messagebox.showinfo(title="Winner",message="The Winner is "+turn.cget("text"))
    resetWindow()
  elif(checkfordraw()==True):
    messagebox.showinfo(title="draw",message="The game is a draw, no winner")
    resetWindow()
  if turn.cget("text")=="X":
    turn.config(text="O")
  else:
    turn.config(text="X")

def checkfordraw():
  if(b1.cget("text")!="-" and b2.cget("text")!="-" and b3.cget("text")!="-" and b4.cget("text")!="-" and b5.cget("text")!="-" and b6.cget("text")!="-" and b7.cget("text")!="-" and b8.cget("text")!="-" and b9.cget("text")!="-"):
    return True
  else:
    return False
def checkforwin():
  if(b1.cget("text")==b2.cget("text") and b2.cget("text")==b3.cget("text") and b3.cget("text")==turn.cget("text")):
    return True
  elif(b4.cget("text")==b5.cget("text") and b5.cget("text")==b6.cget("text") and b6.cget("text")==turn.cget("text")):
    return True
  elif(b7.cget("text")==b8.cget("text") and b8.cget("text")==b9.cget("text") and b9.cget("text")==turn.cget("text")):
    return True
  elif(b1.cget("text")==b4.cget("text") and b4.cget("text")==b7.cget("text") and b7.cget("text")==turn.cget("text")):
    return True
  elif(b2.cget("text")==b5.cget("text") and b5.cget("text")==b8.cget("text") and b8.cget("text")==turn.cget("text")):
    return True
  elif(b3.cget("text")==b6.cget("text") and b6.cget("text")==b9.cget("text") and b9.cget("text")==turn.cget("text")):
    return True
  elif(b1.cget("text")==b5.cget("text") and b5.cget("text")==b9.cget("text") and b9.cget("text")==turn.cget("text")):
    return True
  elif(b7.cget("text")==b5.cget("text") and b5.cget("text")==b3.cget("text") and b3.cget("text")==turn.cget("text")):
    return True
  else:
    return False
b1=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons1Clicked)
b1.place(x=125,y=125)
b2=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons2Clicked)
b2.place(x=200,y=125)
b3=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons3Clicked)
b3.place(x=275,y=125)
b4=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons4Clicked)
b4.place(x=125,y=200)
b5=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons5Clicked)
b5.place(x=200,y=200)
b6=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons6Clicked)
b6.place(x=275,y=200)
b7=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons7Clicked)
b7.place(x=125,y=275)
b8=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons8Clicked)
b8.place(x=200,y=275)
b9=Button(window,text="-",bg="white",fg="black",height=3, width=3,command=Buttons9Clicked)
b9.place(x=275,y=275)


def resetWindow():
  b1.config(text="-")
  b2.config(text="-")
  b3.config(text="-")
  b4.config(text="-")
  b5.config(text="-")
  b6.config(text="-")
  b7.config(text="-")
  b8.config(text="-")
  b9.config(text="-")
  turn.config(text="O")
  
turn=Label(window,text="X")
window.mainloop()
