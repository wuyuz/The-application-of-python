from numpy import roots
from tkinter import *


win = Tk()
win.geometry('500x500')
l1 = Label(win,text='输入系数：').place(x=50,y=50)

num = Entry()
num.place(x=120,y=50)


def getnum():
    num2 = []
    num1 = num.get()

    num2= num1.split(' ')
    ret = roots(num2)
    var.set(ret)

Button(win,text='提交',command=getnum).place(x=170,y=100)

var = StringVar()
Label(win,textvariable=var,).place(x=200,y=300)


# print(roots(a))
win.mainloop()
