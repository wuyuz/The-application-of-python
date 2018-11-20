from aip import AipOcr  # 百度的文字识别
import configparser  # 配置我们的密码

class BaiDuAPI(object):
    '''用于识别文字'''
    def __init__(self):
        # 实例化对象
        target = configparser.ConfigParser()
        target.read('password.ini',encoding='utf-8')  # 读的时候编码
        APPID = target.get('我的工单','APPID')  # 在配置文件中ini的[]里最好是英文，或者编码
        APIKEY= target.get('我的工单','APIKEY')
        SECRETKEY = target.get('我的工单','SECRETKEY')

        # 类内都可用，传给对象的属性
        self.client = AipOcr(APPID,APIKEY,SECRETKEY)

    # 实例方法
    def pictureText(self,filePath):
        # 读取图片
        image = self.getPicture(filePath)
        # 识别图片
        text = self.client.basicGeneral(image)
        for i in text['words_result']:
            for v in i.values():
                print(v)
        # print(text)



    # 读取图片
    @staticmethod
    def getPicture(filePath):
        with open(filePath,'rb') as fp:
            return fp.read()




if __name__ == '__main__':
    baidu = BaiDuAPI()
    baidu.pictureText('imageGrab.png')
