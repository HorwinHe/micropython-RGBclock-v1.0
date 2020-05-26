"""
@Description: In User Settings Edit

@作者: 就酱紫扯创意

@时间: 2019-08-23 21:25:31

@最后编辑时间: 2019-08-24 19:16:23

@最后编辑者: 就酱紫扯创意

"""
import network
#import webrepl
import os
from wifi_conf import *

sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
    print("connecting to network...")
    sta_if.active(True)
    sta_if.connect(wifiName, wifiPdWord) # 此处输入无线网络的账号密码
    while not sta_if.isconnected(): #检查网络是否连接成功
        pass
print("network config:", sta_if.ifconfig())

#webrepl.start()





