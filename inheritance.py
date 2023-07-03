
class Animal:
    def __init__(self,name,color):
        self.name = name
        self.color = color

    def speak(self):
        raise NotImplementedError("Child class must  implement this method")


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
       return "Meows!"


class Cow(Animal):
    def speak(self):
        return "moo!"


# Create an object
dog = Dog("Tom","brown")
print(dog.name)
print(dog.color)
print(dog.speak())
cat = Cat("Minnie","black and white")
print(cat.name)
print(cat.color)
print(cat.speak())
cow = Cow("Rose","brown")
print(cow.name)
print(cow.color)
print(cow.speak())
