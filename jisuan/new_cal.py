# import numpy as np
#
# # a = np.array([[1,-1],[-1,1]])
# a = np.array([[1,-1,0,0,0,0],[-1,2,-1,0,0,0],[0,-1,2,-1,0,0],[0,0,-1,2,-1,0],[0,0,0,-1,2,-1],[0,0,0,0,-1,1]])
# b = np.linalg.eig(a)
# # print(b[0])
#
# q = np.poly1d(b[0],True)
# print(q)

from numpy import roots,poly1d,array,linalg
from tkinter import *



win = Tk()
win.geometry('500x500')
win.title('牛逼！')
l1 = Label(win,text='输入 ：').place(x=50,y=50)

num = Entry(win,width=50,)
num.place(x=120,y=50)


def getnum():
    num2 = []
    num1 = num.get()
    a = array([eval(num1)])
    b = linalg.eig(a)

    # ret = roots(num2)
    ret1 =[]
    for i in b[0][0]:
        ret1.append(round(i,3))
    # var.set(round(b[0][0],4)) # 打印根
    var.set(ret1)

    sum = 0
    for i in range(len(ret1)):
        sum += ret1[i]
    avg = sum/len(ret1)
    var1.set(round(avg,4))

    all_sum = 0
    for i in range(len(ret1)):
        all_sum += abs(ret1[i]-avg)
    var2.set(round(all_sum,4))  # 打印求和函数

    q = poly1d(b[0][0],True)
    var3.set(q)

Button(win,text='提交',command=getnum).place(x=170,y=100)

# 根的文本框
var = StringVar()
l2= Label(win,text='根的列表：').place(x=50,y=150)
Label(win,textvariable=var,bg='#838B83').place(x=110,y=150)

# 平均值的文本框
var1 = StringVar()
l2= Label(win,text='平均值：').place(x=50,y=230)
Label(win,textvariable=var1,bg='#FF4040').place(x=110,y=230)

# 求绝对值的文本框
var2 = StringVar()
l2= Label(win,text='求和 ：').place(x=50,y=310)
Label(win,textvariable=var2,bg='#FF7256').place(x=110,y=310)

var3 = StringVar()
l2= Label(win,text='多项式 ：').place(x=50,y=380)
Label(win,textvariable=var3,bg='#EE7256').place(x=110,y=380)

win.mainloop()
