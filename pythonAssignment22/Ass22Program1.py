class Demo:
    Value = 10

    def __init__(self, No1, No2):
        self.No1 = No1
        self.No2 = No2
    
    def Fun(self):
        print("Value of instance variable no1 and no2 inside fun is : ",self.No1,self.No2)

    def Gun(self):
        print("Value of instance variable no1 and no2 inside gun is : ",self.No1,self.No2)

obj1 = Demo(11, 21)
obj2 = Demo(51, 101)

obj1.Fun()
obj2.Fun()
obj1.Gun()
obj2.Gun()