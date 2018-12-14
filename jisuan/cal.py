from numpy import roots
from tkinter import *


win = Tk()
win.geometry('500x600')
l1 = Label(win,text='输入系数：').place(x=50,y=50)

num = Entry()
num.place(x=120,y=50)


def getnum():
    num2 = []
    num1 = num.get()
    num2= num1.split(' ')
    ret = roots(num2)
    var.set(ret)  # 打印根
    
    sum = 0
    for i in range(len(ret)):
        sum += i
    avg = sum/len(ret)
    var1.set(avg)
    
    all_sum = 0
    for i in range(len(ret)):
        all_sum += abs(ret[i]-avg)
    var2.set(all_sum)  # 打印求和函数
    
Button(win,text='提交',command=getnum).place(x=170,y=100)

# 根的文本框
var = StringVar()
l2= Label(win,text='根的列表：').place(x=100,y=300)
Label(win,textvariable=var，bg='red').place(x=200,y=300)

# 平均值的文本框
var1 = StringVar()
l2= Label(win,text='平均值：').place(x=100,y=450)
Label(win,textvariable=var1,bg='blue').place(x=200,y=450)

# 求绝对值的文本框
var2 = StringVar()
l2= Label(win,text='求和：').place(x=100,y=500)
Label(win,textvariable=var2,bg='green').palce(x=200,y=500)

win.mainloop()
