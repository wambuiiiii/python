class people:
    def __init__(self,name,gender,age):
        self.myname=name
        self.mygender=gender
        self.myage=age
    def display(self):
        print(self.myname,self.mygender,self.myage)
myobj=people("Kani","Female",19)
myobj.display()
myobj=people("saskia","male",69)
myobj.display()
myobj=people("Benja","male",69)
myobj.display()