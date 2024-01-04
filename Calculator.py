from tkinter import *
from tkinter import messagebox

window = Tk()
window.title("Calculator")
window.geometry("600x400")


def button1clicked():
  button1 = l1.cget("text")
  button1 = button1 + "1"
  l1.config(text=button1)


def button2clicked():
  button2 = l1.cget("text")
  button2 = button2 + "2"
  l1.config(text=button2)


def button3clicked():
  button3 = l1.cget("text")
  button3 = button3 + "3"
  l1.config(text=button3)


def button4clicked():
  button4 = l1.cget("text")
  button4 = button4 + "4"
  l1.config(text=button4)


def button5clicked():
  button5 = l1.cget("text")
  button5 = button5 + "5"
  l1.config(text=button5)


def button6clicked():
  button6 = l1.cget("text")
  button6 = button6 + "6"
  l1.config(text=button6)


def button7clicked():
  button7 = l1.cget("text")
  button7 = button7 + "7"
  l1.config(text=button7)


def button8clicked():
  button8 = l1.cget("text")
  button8 = button8 + "8"
  l1.config(text=button8)


def button9clicked():
  button9 = l1.cget("text")
  button9 = button9 + "9"
  l1.config(text=button9)


def button0clicked():
  button0 = l1.cget("text")
  button0 = button0 + "0"
  l1.config(text=button0)


def decimalClicked():
  buttonPoint = l1.cget("text")
  buttonPoint = buttonPoint + "."
  l1.config(text=buttonPoint)


def Cclicked():
  buttonC = l1.config(text="")


def PlusClicked():
  buttonPlus = l1.cget("text")
  l2.config(text=buttonPlus)
  l3.config(text="+")
  l1.config(text="")


def MinusClicked():
  buttonMinus = l1.cget("text")
  l2.config(text=buttonMinus)
  l3.config(text="-")
  l1.config(text="")


def TimesClicked():
  buttonTimes = l1.cget("text")
  l2.config(text=buttonTimes)
  l3.config(text="*")
  l1.config(text="")


def DiviClicked():
  buttonDivison = l1.cget("text")
  l2.config(text=buttonDivison)
  l3.config(text="/")
  l1.config(text="")


def EqualClicked():
  buttonEqual = float(l1.cget("text"))
  p = float(l2.cget("text"))
  d = l3.cget("text")
  if (d == "+"):
    answer = p + buttonEqual
  elif (d == "-"):
    answer = p - buttonEqual
  elif (d == "*"):
    answer = p * buttonEqual
  elif (d == "/"):
    answer = p / buttonEqual
  l1.config(text=str(answer))


l1 = Label(window, text='', bg='green', fg='white', height=3, width=35)
l2 = Label(window, text='')
l3 = Label(window, text='')
l1.place(x=125, y=50)
b1 = Button(window,
            text="1",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button1clicked)
b1.place(x=125, y=125)
b2 = Button(window,
            text="2",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button2clicked)
b2.place(x=200, y=125)
b3 = Button(window,
            text="3",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button3clicked)
b3.place(x=275, y=125)
b4 = Button(window,
            text="4",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button4clicked)
b4.place(x=125, y=200)
b5 = Button(window,
            text="5",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button5clicked)
b5.place(x=200, y=200)
b6 = Button(window,
            text="6",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button6clicked)
b6.place(x=275, y=200)
b7 = Button(window,
            text="7",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button7clicked)
b7.place(x=125, y=275)
b8 = Button(window,
            text="8",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button8clicked)
b8.place(x=200, y=275)
b9 = Button(window,
            text="9",
            bg="white",
            fg="black",
            height=3,
            width=3,
            command=button9clicked)
b9.place(x=275, y=275)
b10 = Button(window,
             text="0",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=button0clicked)
b10.place(x=125, y=350)
b11 = Button(window,
             text="C",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=Cclicked)
b11.place(x=200, y=350)
b12 = Button(window,
             text="+",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=PlusClicked)
b12.place(x=350, y=125)
b13 = Button(window,
             text="-",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=MinusClicked)
b13.place(x=350, y=200)
b14 = Button(window,
             text="*",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=TimesClicked)
b14.place(x=350, y=275)
b15 = Button(window,
             text="/",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=DiviClicked)
b15.place(x=350, y=350)
b16 = Button(window,
             text="=",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=EqualClicked)
b16.place(x=275, y=350)
b17 = Button(window,
             text=".",
             bg="white",
             fg="black",
             height=3,
             width=3,
             command=decimalClicked)
b17.place(x=425, y=350)
window.mainloop()
