#oop-object oriented programming
#1.define  a class(blueprint)
class Student:
    #attributes-age,name,height,course
    #methods-display_details,display_email 
    #constructor: runs automatically when you create a new object
    def __init__(self,name,course,age):
        self.name=name
        self.course=course
        self.age=age
    #method for display details
    def info(self):
        return f"student name is {self.name} and learning {self.course} and {self.age} years old" 
#2 create an object
#object is an instance of a class
st1=Student("mary","mit",20)
st2=Student("william","cybersecurity",22)
#access our attributes
print(st1.name)
print(st1.course)
print(st1.age)
#calling the info() method
print(st1.info())

        