import time
from car import Car
class Wei:
    def __init__(self,level,wei_price=0,car=Car(),where='停车位',count=50):
        self.level=level
        self.wei_price=wei_price
        self.car=car
        self.where=where
        self.count=count
        self.type()
    def type(self):
        if self.level == '3':
            self.wei_price=10
        elif self.level == '2':
            self.wei_price=7
            self.count=40
        elif self.level == '1':
            self.wei_price=5
            self.count=20
    def enter(self):
        self.count-=1
        print('进入',self.where,'等级',self.level,'单价',self.wei_price,'剩余停车位',self.count)
    def out(self):
        self.count+=1
        print('离开',self.where,'剩余停车位',self.count)
wei=Wei('1')