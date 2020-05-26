"""
@Description: In User Settings Edit

@作者: 就酱紫扯创意

@时间: 2019-08-23 21:25:31

@最后编辑时间: 2019-08-24 19:16:23

@最后编辑者: 就酱紫扯创意

"""
from machine import Pin, RTC, Timer
from neopixel import NeoPixel
from Numbers import *
import time, urequests,ujson


######  获取网络时间  ######
def Get_Time():
    URL = "http://api.k780.com/?app=life.time&appkey=41512&sign=58fd2e88ee2af2a14def78ab9ba92abd&format=json"
    res = urequests.get(URL).text
    j = ujson.loads(res)
    Time_All = j["result"]["datetime_1"].split()[1]
    Time = Time_All.split(':')
    Year_All = j["result"]["datetime_1"].split()[0]
    Year = Year_All.split('-')
    DateTime = (int(Year[0]), int(Year[1]), int(Year[2]), 1, int(Time[0]),
                int(Time[1]), int(Time[2]), 0)
    return DateTime
    '''
    week1 = j["result"]["week_1"]
    week = ''
    T = list(Time)

    if week1 == '0':
        week = '7'
    else:
        week = week1
    '''

###### 显示RTC时间 ######
def Display_Time():
    
    global Hours1_1,Hours1_2,Hours2_1,Hours2_2,Mints1_1,Mints1_2,Mints2_1,Mints2_2,Secos1,Secos2

    Time = str(rtc.datetime())[1:-1].split(',')
    Minutes = Time[5]

    if len(Time[4]) < 3:
		   np[0] = (228,0,127)
		   np[1] = (228,0,127)
		   np[Hours1_1] = (0,0,0)
		   np[Hours1_2] = (0,0,0)
		   np[Hours2_1] = (0,0,0)
		   np[Hours2_2] = (0,0,0)
		   np[int(Hours_2[int(Time[4][1])][:2])] = (228,0,127)
		   np[int(Hours_2[int(Time[4][1])][-2:])] = (228,0,127)
		   np.write()

		   Hours2_1 = int(Hours_2[int(Time[4][1])][:2])
		   Hours2_2 = int(Hours_2[int(Time[4][1])][-2:])

    else:
	    np[0] = (0,0,0)
	    np[1] = (0,0,0)
	    np[Hours1_1] = (0,0,0)
	    np[Hours1_2] = (0,0,0)
	    np[Hours2_1] = (0,0,0)
	    np[Hours2_2] = (0,0,0)
	    np[int(Hours_1[int(Time[4][1])][:2])] = (228,0,127)
	    np[int(Hours_1[int(Time[4][1])][-2:])] = (228,0,127)
	    np[int(Hours_2[int(Time[4][2])][:2])] = (228,0,127)
	    np[int(Hours_2[int(Time[4][2])][-2:])] = (228,0,127)
	    np.write()

	    Hours1_1 = int(Hours_1[int(Time[4][1])][:2])
	    Hours1_2 = int(Hours_1[int(Time[4][1])][-2:])
	    Hours2_1 = int(Hours_2[int(Time[4][2])][:2])
	    Hours2_2 = int(Hours_2[int(Time[4][2])][-2:])


    if len(Time[5]) < 3:
	    np[40] = (228,0,127)
	    np[41] = (228,0,127)
	    np[Mints1_1] = (0,0,0)
	    np[Mints1_2] = (0,0,0)
	    np[Mints2_1] = (0,0,0)
	    np[Mints2_2] = (0,0,0)
	    np[int(Mints_2[int(Time[5][1])][:2])] = (228,0,127)
	    np[int(Mints_2[int(Time[5][1])][-2:])] = (228,0,127)
	    np.write()

	    Mints2_1 = int(Mints_2[int(Time[5][1])][:2])
	    Mints2_2 = int(Mints_2[int(Time[5][1])][-2:])

    else:
	    np[40] = (0,0,0)
	    np[41] = (0,0,0)
	    np[Mints1_1] = (0,0,0)
	    np[Mints1_2] = (0,0,0)
	    np[Mints2_1] = (0,0,0)
	    np[Mints2_2] = (0,0,0)
	    np[int(Mints_1[int(Time[5][1])][:2])] = (228,0,127)
	    np[int(Mints_1[int(Time[5][1])][-2:])] = (228,0,127)
	    np[int(Mints_2[int(Time[5][2])][:2])] = (228,0,127)
	    np[int(Mints_2[int(Time[5][2])][-2:])] = (228,0,127)
	    np.write()

	    Mints1_1 = int(Mints_1[int(Time[5][1])][:2])
	    Mints1_2 = int(Mints_1[int(Time[5][1])][-2:])
	    Mints2_1 = int(Mints_2[int(Time[5][2])][:2])
	    Mints2_2 = int(Mints_2[int(Time[5][2])][-2:])


    if len(Time[6]) < 3:
	    np[80] = (0,71,157)
	    np[Secos1] = (0,0,0)
	    np[Secos2] = (0,0,0)
	    np[int(Secos_2[int(Time[6][1])])] = (0,71,157)
	    np.write()

	    Secos2 = int(Secos_2[int(Time[6][1])])
	
    else:
	    np[80] = (0,0,0)
	    np[Secos1] = (0,0,0)
	    np[Secos2] = (0,0,0)
	    np[int(Secos_1[int(Time[6][1])])] = (0,71,157)
	    np[int(Secos_2[int(Time[6][2])])] = (0,71,157)
	    np.write()

	    Secos1 = int(Secos_1[int(Time[6][1])])
	    Secos2 = int(Secos_2[int(Time[6][2])])


    if int(Minutes.lstrip()) == 30:
        rtc.datetime(Get_Time())


###### RGB效果清除 ######
def Clear(i):
	np[i] = (0, 0, 0)
	np.write()

def Cycle(r, g, b, wait):
	for i in Secos:
		for j in Secos:
			np[j] = (0, 0, 0)
		np[i % n] = (r, g, b)
		np.write()
		time.sleep_ms(wait)


def Try_Start():
    try:
        tim = Timer(1)
        tim.init(period=500,
                 mode=Timer.PERIODIC,
                 callback=lambda t: Display_Time())
        
    except:
        rtc.datetime(Get_Time())
        tim.deinit()
        Try_Start()


if __name__ == '__main__':
    n = 100
    pin = Pin(13, Pin.OUT)
    np = NeoPixel(pin, n)
    
    (Hours1_1,Hours1_2,Hours2_1,Hours2_2) = (0,0,0,0)
    (Mints1_1,Mints1_2,Mints2_1,Mints2_2) = (0,0,0,0)
    Secos1 = 0
    Secos2 = 0

    #RGB = (255,20,147)

    #Np_List = []
    
    rtc = RTC()
    rtc.datetime(Get_Time())
    Try_Start()

