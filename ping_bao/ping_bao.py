from tkinter import *
from random import randint
import tkinter.font as tkFont
import linecache

class Screensaver():
    txt_1 = []
    i = 1
    def __init__(self):
        self.win = Tk()
        self.ft = tkFont.Font(family='Fixdsys', size=30, weight=tkFont.BOLD)
        self.width = self.win.winfo_screenwidth()
        self.height= self.win.winfo_screenheight()
        self.win.overrideredirect(1)
        self.win.overrideredirect(1)
        self.win.attributes('-alpha',0.3)
        self.list_ =[]

        # 绑定事件
        self.win.bind('<Any-Button>',self.exit_screensaver)
        self.canvas=Canvas(self.win,width=self.width,height=self.height,bg='#00FFFF')
        self.canvas.pack()
        self.birth_list()
        self.run_screensaver()
        self.win.mainloop()

    # 生成文本列表
    def birth_list(self):
        i = randint(0,2064)
        self.str_text = linecache.getlines('six.txt')[i:i+21]
        if self.i == 1:
            for my_text in self.str_text:
                txt = Text_screen(self.canvas,self.ft,self.width,self.height,my_text)
                self.list_.append(txt)
        else: pass
    def exit_screensaver(self,event):   # 这里必须要个参数event
        self.win.destroy()

    def run_screensaver(self):
        if self.i == 1:
            for emumt in self.list_:
                emumt.move_text()
                if emumt.x1<= -30:
                    emumt
                    self.i = -1
                    self.delect()
                    self.list_ =[]
                    self.birth_list()
                    for my_text in self.str_text:
                        txt = Text_screen(self.canvas,self.ft,self.width,self.height,my_text)
                        self.list_.append(txt)
                    break
        else:
            self.i *= -1
        self.canvas.after(1,self.run_screensaver)

    def delect(self):
        for em in self.list_:
            self.canvas.delete(em.item)

class Text_screen():
    list_box = [i for i in range(20,1080,50)]  # 22 个对象
    i = 0
    def __init__(self,canvas,ft,width,height,text_1):
        self.canvas = canvas
        self.ft = ft
        self.text_1 = text_1
        self.x_pos = width
        self.x_move = -1
        self.create_text()

    def create_text(self):
        self.x1 = self.x_pos-100
        self.item = self.canvas.create_text(self.x1,self.list_box[Text_screen.i],text=self.text_1,font=self.ft,fill='red',anchor=NW)
        if Text_screen.i == len(Text_screen.list_box)-1:
            Text_screen.i = 0
        else: Text_screen.i += 1

    def move_text(self):
        self.canvas.move(self.item, self.x_move,0)
        self.x1 += self.x_move


Screensaver()
