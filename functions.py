#function are reusable block of code that does a specific task
# def functioname():
    #body of the function
#function only runs when called
#functioname()
def greet():
    print("hello good evening!!")
#calling the function
greet()
greet()
#function with parameter
def hello(first_name):
    print("hey",first_name)
#calling the function
hello("jane")
hello("joyce")
#function with multiple parameters
def display_details(name,age,course="mit"):
    print(f"my name is {name} and i am {age} years old and i am studying {course}")
#calling the function
display_details("cate",19)
display_details("william",20,"data science")
#a function that calculates area of rectangle hint area=l*w
#a function that calculates area of circle a=3.14*r*r
#function that checks if a number is evenorodd hint num%2==0
#function that multiplies 3 numbers
#lambda#function that has return keyword-returns  a value when called
#function that adds two numbers and returns the sum
def addTwoNumbers(a,b):
    sum=a+b
    return sum
#calling the function and printing the returned value
print(addTwoNumbers(30,70))
print(addTwoNumbers(52,78))
#calling the function and store the returned value in a variable
result=addTwoNumbers(29,45)
print("The sum is",result)
#lambda function/anonymous function
#lambda argurments:expresion
multiply= lambda a,b,c:a*b*c
print(multiply(4,8,7))
