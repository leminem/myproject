# 使用面向对象的思路实现『停车收费』场景：
# 1. 车主开车进入停车场，产生停车记录，
# 2. 车主开车继续向前，将车停到车位上，修改前面的停车记录，
# 3. 车主停车完成，
# 一段时间(购物、吃饭...)之后，车主驾车准备离开停车场，
# 4. 车主开车离开车位，修改停车记录，
# 5. 车主开车到达出口，系统根据停车的时间生成订单，
# 6. 车主缴纳停车费，
# 7. 车主离开停车场。
# 至此，整个停车收费的场景完成。
from people import People
class Car:
    def __init__(self,card='辽A45888',owner=People()):
        self.card=card
        self.owner=owner
    def info(self):
        print('姓名：',self.owner.name,'电话：',self.owner.phone,'车牌:',self.card)    
 

