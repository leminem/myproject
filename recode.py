from car import Car
from part_wei import Wei
import time
class Recode:
    def __init__(self,car=Car(),wei=Wei('1'),enter_c_time=0,out_c_time=0,enter_w_time=0,out_w_time=0):
        self.car=car
        self.wei=wei
        self.enter_c_time=enter_c_time
        self.out_c_time=out_c_time
        self.enter_w_time=enter_w_time
        self.out_w_time=out_w_time
    def list(self):
        randomlist=''
        park_time = time.mktime(time.strptime(self.out_c_time,"%Y-%m-%d %H:%M:%S"))-time.mktime(time.strptime(self.enter_c_time,"%Y-%m-%d %H:%M:%S"))
        h= park_time // 3600
        m = (park_time - h * 3600) // 60
        s = park_time - h * 3600 - m * 60
        host_time = "%.0f时%.0f分%.0f秒" % (h, m, s)
        randomlist=str(h)[:-2]+str(m)[:-2]+str(s)[:-2]
        return randomlist