from tkinter import *   # 这里显示的是 __all__ = [a,b]
from tkinter import messagebox  # 不是所有的参数都在里面
from icon import img   # 在icon中找到我们编码的图片文件
import base64    # 将会用它解码图片
import os

def closeWindow():
    # 当用户点击叉时，触发的函数
    messagebox.showinfo(title='警告',message='不许关闭，好好回答') # 当然还有showerror提示
    return

def closeallWindows():
    # 销毁所有窗口
    window.destroy()

def love():  # 响应喜欢后的窗口
    love = Toplevel(window)   # 是一个独立的顶级窗口
    love.geometry('200x150+700+400')
    love.title('好巧，我也是！')
    label = Label(love,text='好巧，我也是',font=('微软雅黑',15))
    label.pack()
    label1 = Label(love, text='留个微信可以吗？', font=('微软雅黑', 15))
    label1.pack()
    entry = Entry(love,font=('微软雅黑',15))
    entry.pack()
    btn =Button(love,text= '确定',width=10,height=2,command=closeallWindows)
    btn.pack()
    # 在这个窗口中也要定义关闭窗口的作用
    love.protocol('WM_DELETE_WINDOW',closelove)

def closelove():
    messagebox.showinfo('不再考虑一下吗？',message='再考虑一下吧！')
    return

def nolove():   # 不喜欢出发的方法
    no_love = Toplevel(window)
    no_love.geometry('200x100+610+260')
    no_love.title('再考虑考虑呗')
    label = Label(no_love,text='再考虑考虑呗',font=('微软雅黑',15))
    label.pack()
    # 窗口.destory 就是销毁当前窗口
    btn =Button(no_love,text= '好的',width=10,height=2,command=no_love.destroy)
    btn.pack()
    # 修改叉叉窗口
    no_love.protocol('WM_DELETE_WINDOW',closenolove)

def closenolove():
    # 一直触发这个方法 回调函数
    nolove()

# 创建窗口对象
window = Tk()
# 设置窗口标题
window.title('喜欢我吗？')
# 设置窗口大小 前两个参数是窗口大小，后两个是屏幕位置
window.geometry('380x420+590+230')
# 点击用户关闭，触发函数
window.protocol('WM_DELETE_WINDOW',closeWindow)

# 标签控件
label1 = Label(window,text='hey，小姐姐！',font=('微软雅黑',15),fg='red')
# 定位，grid 网格式布局，还有：pack 包定位 place
label1.grid()

label2 = Label(window,text='喜欢我吗？',font=('微软雅黑',23))
# 这里需要定位了，使其右对齐，也就是网格的1，从0开始,sticky是对齐方式，E就是东
label2.grid(row=1,column=1,sticky=E)


# 引入图片
tmp = open('tmp.png','wb+')
tmp.write(base64.b64decode(img))
tmp.close()

# 显示图片
photo = PhotoImage(file = './tmp.png')   # 这里将会自动在exe文件下生成一个图片文件
os.remove('./tmp.png')  # 生成后会自动删除图片
imageLable = Label(window,image=photo)
# 这里不能写row=2,column=0，这里会显示的很鸡肋，需要合并列
imageLable.grid(row=2,columnspan=2)
# 按钮 设置参数


btn1 = Button(window,text='喜欢',width=15,height=2,command=love)
btn1.grid(row=3,column=0,sticky=W)

btn2 = Button(window,text='不喜欢',command=nolove)
btn2.grid(row=3,column=1,sticky=E)

# 显示窗口， 消息循环
window.mainloop()
