from recode import Recode
import time
import random
class Order:
    def __init__(self,order_number=random.randint(1,10000),recode=Recode()):
        self.order_number=order_number
        self.recode=recode
    def list(self):
        self.recode.car.info()
        random=self.recode.list()+str(self.order_number)
        print('订单号：',random)
    def cost(self):
        park_time = time.mktime(time.strptime(self.recode.out_c_time,"%Y-%m-%d %H:%M:%S"))-time.mktime(time.strptime(self.recode.enter_c_time,"%Y-%m-%d %H:%M:%S"))
        h= park_time // 3600
        m = (park_time - h * 3600) // 60
        s = park_time - h * 3600 - m * 60
        host_time = "%.0f时%.0f分%.0f秒" % (h, m, s)
        cost = ((park_time) // 3600) * self.recode.wei.wei_price
        print('总停车时间',host_time,'花费',cost,'元')

    
