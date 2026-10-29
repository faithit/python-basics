#inheritance is a concept in oop that allows a child/subclass/derived class
#to inherit methods and attributes from parent/base/superclass

#parent class
class Animal:
    #attributes habitat,age,name
    #constructor
    def __init__ (self,name,age,habitat):
        self.name=name
        self.age=age
        self.habitat=habitat
    def __str__(self):
        return f"The animal name is {self.name}  and its {self.age} years old and lives in {self.habitat}"
    def speek(self):
        return f"{self.name} makes a sound"
#child class-inherets from animal class
class Dog(Animal):
    def __init__(self,name,age,habitat,breed):
        Animal.__init__(self,name,age,habitat)
        self.breed=breed
    def speek(self):
        return f"{self.name} barks barks" #method overiding
    def info(self):
        return f"{self.name} is a {self.breed}
#cat class that inherits from animal

#creating a dog object
dog1=Dog("simba",2,"land","german sherperd")
print(dog1.name)
print(dog1.age)
print(dog1.habitat)
print(dog1)
print(dog1.info())
#calling the speek
print(dog1.speek())


        