class Magari:
    def __init__(self,modelname,color,year,capacity):
        self.model=modelname
        self.mycolor=color
        self.myyear=year
        self.mycapacity=capacity
    def onyesha(self):
        print(self.model,self.mycolor,self.myyear,self.mycapacity)
        # create an object
        # to access a class use an object
myobj=Magari("Toyota","white",2034,20)
# call the object objectname.classname
myobj.onyesha()
myobj=Magari("Nissan","blue",2022,20)
myobj.onyesha()