

import time
import sys
# 控制键盘事件
import keyboard
from PIL import ImageGrab
from baidu import BaiDuAPI

def screenShot():
    # 等待两个键结束，然后再操作剪切板的数据
    if keyboard.wait(hotkey='ctrl+alt+a') == None:
        if keyboard.wait(hotkey='enter') == None:
            # 因为程序很快，刚截取的图片还没保存就执行了，也就是执行的上次图片
            time.sleep(0.01)
            # 读取剪切板里面的照片
            im = ImageGrab.grabclipboard()
            # 保存 在当前文件下
            im.save('imageGrab.png')


for _ in range(sys.maxsize):
    screenShot()
    print('截取一张图片,读取中……')
    baidu = BaiDuAPI()
    baidu.pictureText('imageGrab.png')
