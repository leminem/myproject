from recode import Recode
from order import Order
import time
from part_wei import Wei
from car import Car
class Chang:
    def __init__(self,car=Car(),wei=Wei('1'),recode=Recode(),where='停车场',order=Order()):
        self.car=car
        self.wei=wei
        self.where=where
        self.recode=recode
        self.order=order
    def enter(self):
        self.car.info()
        self.car.owner.drive()
        print(self.where)
        self.order.recode.enter_c_time='2018-11-22 11:11:10'
        print('停车记录：时间',self.order.recode.enter_c_time)
        self.wei.enter()
        self.order.recode.enter_w_time='2018-11-22 12:14:08'
        print('停车记录：时间',self.order.recode.enter_w_time)
    def out(self):
        self.wei.out()
        self.order.recode.out_w_time='2018-11-22 18:13:07'
        print('停车记录：时间',self.order.recode.out_w_time)
        self.car.owner.stop()
        print(self.where)
        self.order.recode.out_c_time='2018-11-22 21:12:19'
        print('停车记录：时间',self.order.recode.out_c_time)
        self.order.list()
        self.order.cost()
        # self.order.list()
        # self.order.cost()
        # print(random)


chang=Chang()
chang.enter()
chang.out()